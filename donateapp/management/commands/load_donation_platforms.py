from django.core.management.base import BaseCommand
from donateapp.models import DonationPlatform

class Command(BaseCommand):
    help = 'Loads initial donation platforms data'

    def handle(self, *args, **kwargs):
        platforms_data = [
            {
                "name": "Dubai Cares",
                "website": "https://www.dubaicares.ae",
                "description": "A UAE-based philanthropic organization focused on education in developing countries.",
                "logo_url": "https://www.dubaicares.ae/images/logo.svg",
                "location": "Dubai, UAE",
                "contact_email": "info@dubaicares.ae",
                "phone": "+971 4 450 4550"
            },
            {
                "name": "Emirates Red Crescent",
                "website": "https://www.rcuae.ae",
                "description": "Humanitarian aid and emergency relief provider both locally and internationally.",
                "logo_url": "https://www.rcuae.ae/images/logo.png",
                "location": "Abu Dhabi, UAE",
                "contact_email": "info@rcuae.ae",
                "phone": "+971 2 444 0500"
            },
            {
                "name": "Dar Al Ber Society",
                "website": "https://www.daralber.ae",
                "description": "Supports needy families, education, health, and emergency relief projects.",
                "logo_url": "https://www.daralber.ae/images/logo.png",
                "location": "Dubai, UAE",
                "contact_email": "info@daralber.ae",
                "phone": "+971 4 352 3333"
            },
            {
                "name": "Beit Al Khair Society",
                "website": "https://www.beitalkhair.org",
                "description": "Specialized in local community welfare through zakat and charity programs.",
                "logo_url": "https://www.beitalkhair.org/images/logo.png",
                "location": "Dubai, UAE",
                "contact_email": "info@beitalkhair.org",
                "phone": "+971 4 336 6613"
            },
            {
                "name": "Sharjah Charity International",
                "website": "https://www.sharjahcharity.ae",
                "description": "Conducts relief operations, orphan sponsorship, and health campaigns.",
                "logo_url": "https://www.sharjahcharity.ae/images/logo.png",
                "location": "Sharjah, UAE",
                "contact_email": "info@sharjahcharity.ae",
                "phone": "+971 6 599 9999"
            },
            {
                "name": "Zayed Charitable and Humanitarian Foundation",
                "website": "https://www.zayedchf.gov.ae",
                "description": "Philanthropic work focusing on education, health, and housing.",
                "logo_url": "https://www.zayedchf.gov.ae/images/logo.png",
                "location": "Abu Dhabi, UAE",
                "contact_email": "info@zayedchf.gov.ae",
                "phone": "+971 2 651 6666"
            },
            {
                "name": "Al Jalila Foundation",
                "website": "https://www.aljalilafoundation.ae",
                "description": "Invests in medical education, research, and treatment in the UAE.",
                "logo_url": "https://www.aljalilafoundation.ae/assets/img/logo.png",
                "location": "Dubai, UAE",
                "contact_email": "info@aljalilafoundation.ae",
                "phone": "+971 4 383 8010"
            },
            {
                "name": "Dubai Charity Association",
                "website": "https://www.dubaicharity.org",
                "description": "Provides education, food, water, and emergency relief locally and abroad.",
                "logo_url": "https://www.dubaicharity.org/images/logo.png",
                "location": "Dubai, UAE",
                "contact_email": "info@dubaicharity.org",
                "phone": "+971 4 268 4644"
            },
            {
                "name": "1 Billion Meals Campaign",
                "website": "https://www.1billionmeals.ae",
                "description": "MENA's largest food drive, led by MBR Global Initiatives.",
                "logo_url": "https://www.1billionmeals.ae/logo.png",
                "location": "Dubai, UAE",
                "contact_email": "info@mbrgi.ae",
                "phone": "+971 4 423 3333"
            },
            {
                "name": "National CSR Fund (Majra)",
                "website": "https://www.mafra.gov.ae",
                "description": "Federal initiative supporting sustainable corporate social responsibility.",
                "logo_url": "https://www.mafra.gov.ae/assets/logo.png",
                "location": "Abu Dhabi, UAE",
                "contact_email": "info@mafra.gov.ae",
                "phone": "+971 2 666 6000"
            }
        ]

        # Clear existing data
        DonationPlatform.objects.all().delete()

        # Create new platforms
        for platform_data in platforms_data:
            DonationPlatform.objects.create(**platform_data)

        self.stdout.write(self.style.SUCCESS('Successfully loaded donation platforms data')) 