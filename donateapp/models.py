from django.db import models

# Create your models here.

class DonationPlatform(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo_url = models.URLField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    contact_email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Donation Platform"
        verbose_name_plural = "Donation Platforms"

class Donation(models.Model):
    platform = models.ForeignKey(DonationPlatform, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    card_number = models.CharField(max_length=16)  # Last 4 digits only
    card_expiry = models.CharField(max_length=5)
    card_cvc = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')  # pending, success, failed
    
    def __str__(self):
        return f"{self.donor_name} - {self.amount} - {self.platform.name}"
    
    class Meta:
        verbose_name = "Donation"
        verbose_name_plural = "Donations"
