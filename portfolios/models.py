from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os




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
    background_image = models.ImageField(upload_to='backgrounds/', null=True, blank=True)
    
    selected_background = models.CharField(max_length=6, default='bg0')
    

    userUrl= models.CharField(max_length=100, blank=True, null=True,unique=True)
    

    def __str__(self):
        return self.name if self.name else "User Info"

class Highlight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='highlights')  # Allows multiple highlights per user
    highlight_thumbnail_image = models.ImageField(upload_to='thumbnail_images/', blank=True, null=True)
    highlight_title = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)  # Link field for URL

    def __str__(self):
        return self.highlight_title or "Untitled Highlight"
    def save(self, *args, **kwargs):
        # Ensure the user has no more than 7 highlights
        if self.user.highlights.count() >= 7:
            # Delete the oldest highlight (first one ordered by creation date)
            oldest_highlight = self.user.highlights.order_by('id').first()
            if oldest_highlight:
                oldest_highlight.delete()
        
        # Proceed with saving the new highlight
        super().save(*args, **kwargs)


# Section Model - One-to-Many relationship with User
class Section(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sections")  # User can have many sections
    section_title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.section_title

# SectionData Model - One-to-Many relationship with Section
class SectionData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="section_data")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="section_data")  # Each section can have multiple data entries
    main_title = models.CharField(max_length=100)
    desc = models.TextField(max_length=200, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    pic = models.ImageField(upload_to='section_images/', blank=True, null=True)
    
    def __str__(self):
        return self.main_title


@receiver(post_delete, sender=Highlight)
def delete_highlight_image(sender, instance, **kwargs):
    if instance.highlight_thumbnail_image:
        if os.path.isfile(instance.highlight_thumbnail_image.path):
            os.remove(instance.highlight_thumbnail_image.path)

# Define signal to delete file when SectionData instance is deleted
@receiver(post_delete, sender=SectionData)
def delete_sectiondata_image(sender, instance, **kwargs):
    if instance.pic:
        if os.path.isfile(instance.pic.path):
            os.remove(instance.pic.path)
            
@receiver(pre_save, sender=UserInfo)
def delete_old_profile_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            # Get the existing User_Info instance from the database
            old_instance = UserInfo.objects.get(pk=instance.pk)
            # Check if there's an existing image that differs from the new one
            if old_instance.profile_image and old_instance.profile_image != instance.profile_image:
                # Delete the old image file
                if os.path.isfile(old_instance.profile_image.path):
                    os.remove(old_instance.profile_image.path)
        except UserInfo.DoesNotExist:
            # If the User_Info instance is new, nothing to delete
            pass
@receiver(pre_save, sender=UserInfo)
def delete_old_background_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            # Get the existing User_Info instance from the database
            old_instance = UserInfo.objects.get(pk=instance.pk)
            # Check if there's an existing image that differs from the new one
            if old_instance.background_image and old_instance.background_image != instance.background_image:
                # Delete the old image file
                if os.path.isfile(old_instance.background_image.path):
                    os.remove(old_instance.background_image.path)
        except UserInfo.DoesNotExist:
            # If the User_Info instance is new, nothing to delete
            pass

class Alldesigns(models.Model):
    DESIGN_CHOICES = [
        ('designs', 'Designs Folder'),
        ('animated', 'Animated Folder'),
    ]
    
    name = models.CharField(max_length=100)  # Name of the design
    template_file = models.FileField(upload_to='templates/', max_length=255)  # Upload the template file
    location = models.CharField(max_length=10, choices=DESIGN_CHOICES, default='designs')  # Folder choice
    code_name = models.CharField(max_length=6, unique=True)  # Code name for template (bg0, bg1, etc.)

    def __str__(self):
        return self.name
