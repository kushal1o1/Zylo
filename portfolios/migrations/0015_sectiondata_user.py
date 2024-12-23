# Generated by Django 5.0.3 on 2024-11-06 16:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0014_section_sectiondata'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sectiondata',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='section_data', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
