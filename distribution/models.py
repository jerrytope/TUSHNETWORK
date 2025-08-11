from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Release(models.Model):
    RELEASE_TYPE_CHOICES = [
        ('single', 'Single'),
        ('album', 'Album'),
        ('ep', 'EP'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending', 'Pending Review'),
        ('approved', 'Approved'),
        ('live', 'Live'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='releases')
    title = models.CharField(max_length=200)
    artist_name = models.CharField(max_length=100)
    release_type = models.CharField(max_length=10, choices=RELEASE_TYPE_CHOICES)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    cover_art = models.ImageField(upload_to='covers/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.artist_name}"

class Track(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='tracks/')
    track_number = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.track_number}. {self.title}"

class Platform(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='platform_logos/', blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Distribution(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='distributions')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    is_distributed = models.BooleanField(default=False)
    distributed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.release.title} -> {self.platform.name}"