# Generated by Django 5.1.1 on 2024-11-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0019_alter_userinfo_selected_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='backgrounds/'),
        ),
    ]
