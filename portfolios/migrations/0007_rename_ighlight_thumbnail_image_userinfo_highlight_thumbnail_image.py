# Generated by Django 5.0.3 on 2024-09-30 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0006_remove_userinfo_phone_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='ighlight_thumbnail_image',
            new_name='highlight_thumbnail_image',
        ),
    ]
