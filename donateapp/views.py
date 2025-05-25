from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Sum, Count
from .models import DonationPlatform, Donation
from .serializers import (
    DonationPlatformSerializer,
    DonationRequestSerializer,
    DonationResponseSerializer
)

# Create your views here.

class DonationPlatformViewSet(viewsets.ModelViewSet):
    queryset = DonationPlatform.objects.all()
    serializer_class = DonationPlatformSerializer

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        try:
            # Get total donations and amount
            total_donations = Donation.objects.count()
            total_amount = Donation.objects.aggregate(total=Sum('amount'))['total'] or 0

            # Get unique donors count
            unique_donors = Donation.objects.values('donor_email').distinct().count()

            # Get all donation records with platform details
            donation_records = Donation.objects.select_related('platform').values(
                'id',
                'amount',
                'donor_name',
                'donor_email',
                'card_number',
                'card_expiry',
                'status',
                'created_at',
                'platform__name',
                'platform__id'
            ).order_by('-created_at')

            response_data = {
                'overall_statistics': {
                    'total_donations': total_donations,
                    'total_amount': float(total_amount),
                    'unique_donors': unique_donors
                },
                'donation_records': list(donation_records)
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

@method_decorator(csrf_exempt, name='dispatch')
class DonationView(APIView):
    def get(self, request):
        # For testing purposes, return a sample response
        return Response({
            'message': 'This endpoint accepts POST requests with the following format:',
            'example': {
                'donation_id': 3,
                'amount': 250.00,
                'card_number': '4111111111111111',
                'card_expiry': '12/26',
                'card_cvc': '123',
                'donor_name': 'Ali Khan',
                'donor_email': 'ali@example.com'
            }
        })

    def options(self, request, *args, **kwargs):
        response = Response()
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    def post(self, request):
        # Validate request data
        serializer = DonationRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Get validated data
        data = serializer.validated_data
        
        try:
            # Get the platform
            platform = DonationPlatform.objects.get(id=data['donation_id'])
            
            # Create donation record
            donation = Donation.objects.create(
                platform=platform,
                amount=data['amount'],
                donor_name=data['donor_name'],
                donor_email=data['donor_email'],
                card_number=data['card_number'][-4:],  # Store only last 4 digits
                card_expiry=data['card_expiry'],
                card_cvc=data['card_cvc'],
                status='success'
            )

            # Prepare response
            response_data = {
                'status': 'success',
                'message': 'Donation processed successfully',
                'data': {
                    'donation_id': platform.id,
                    'amount': float(donation.amount),
                    'donor_name': donation.donor_name
                }
            }
            
            response = Response(response_data, status=status.HTTP_200_OK)
            response["Access-Control-Allow-Origin"] = "*"
            return response
            
        except DonationPlatform.DoesNotExist:
            return Response(
                {'error': 'Donation platform not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
