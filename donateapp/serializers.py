from rest_framework import serializers
from .models import DonationPlatform, Donation

class DonationPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationPlatform
        fields = ['id', 'name', 'website', 'description', 'logo_url', 'location', 'contact_email', 'phone']

class DonationRequestSerializer(serializers.Serializer):
    donation_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    card_number = serializers.CharField(max_length=16)
    card_expiry = serializers.CharField(max_length=5)
    card_cvc = serializers.CharField(max_length=4)
    donor_name = serializers.CharField(max_length=100)
    donor_email = serializers.EmailField()

    def validate_donation_id(self, value):
        try:
            DonationPlatform.objects.get(id=value)
            return value
        except DonationPlatform.DoesNotExist:
            raise serializers.ValidationError("Invalid donation platform ID")

class DonationResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    message = serializers.CharField()
    data = serializers.DictField() 