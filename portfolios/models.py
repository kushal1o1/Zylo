from django.db import models



class UserInfo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "User Info"

class Question(models.Model):
    text = models.TextField()  # The question text
    order = models.PositiveIntegerField()  # To maintain the order of questions

    def __str__(self):
        return self.text