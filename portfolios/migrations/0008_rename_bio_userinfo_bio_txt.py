# Generated by Django 5.0.3 on 2024-09-30 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0007_rename_ighlight_thumbnail_image_userinfo_highlight_thumbnail_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='bio',
            new_name='bio_txt',
        ),
    ]
