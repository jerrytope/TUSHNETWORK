from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ACCOUNT_TYPE_CHOICES = [
        ('artist', 'Artist'),
        ('label', 'Label'),
    ]
    
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('artiste', 'Artiste Plan'),
        ('artist_plus', 'Artist Plus Plan'),
    ]
    
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, default='artist')
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='free')
    phone_number = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=50, default='Nigeria')
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.account_type})"

class ArtistProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='artist_profile')
    stage_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    social_links = models.JSONField(default=dict, blank=True)
    
    def __str__(self):
        return self.stage_name

class LabelProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='label_profile')
    label_name = models.CharField(max_length=100)
    founded_year = models.IntegerField(null=True, blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.label_name