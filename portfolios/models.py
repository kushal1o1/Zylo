from django.db import models
from django.contrib.auth.models import User



class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
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

    def __str__(self):
        return self.name if self.name else "User Info"
