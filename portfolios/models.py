from django.db import models
from django.contrib.auth.models import User


BACKGROUND_CHOICES = [
        ('bg1', 'Background 1'),
        ('bg2', 'Background 2'),
        ('bg3', 'Background 3'),
        ('bg4', 'Background 4'),
        ('bg5', 'Background 5'),
        ('bg6', 'Background 6'),
        ('bg7', 'Background 7'),
        ('bg8', 'Background 8'),
    ]
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    profession = models.TextField(blank=True, null=True)
    bio_txt = models.TextField(blank=True, null=True)
    
    
    # Social media links
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    tiktok_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    x_link = models.URLField(blank=True, null=True)  
    spotify_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    # Media uploads
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    highlight_thumbnail_image = models.ImageField(upload_to='thumbnail_images/', blank=True, null=True)
    highlight_title = models.CharField(max_length=100, blank=True, null=True)
    
    selected_background = models.CharField(max_length=3, choices=BACKGROUND_CHOICES, default='bg1')

    userUrl= models.CharField(max_length=100, blank=True, null=True,unique=True)
    

    def __str__(self):
        return self.name if self.name else "User Info"
