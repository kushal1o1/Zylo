# Generated by Django 5.0.3 on 2024-10-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0008_rename_bio_userinfo_bio_txt'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='profession',
            field=models.TextField(blank=True, null=True),
        ),
    ]