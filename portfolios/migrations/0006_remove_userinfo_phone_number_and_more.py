# Generated by Django 5.0.3 on 2024-09-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0005_alter_userinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='highlight_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='ighlight_thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail_images/'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='linkedin_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='spotify_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='tiktok_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='x_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
