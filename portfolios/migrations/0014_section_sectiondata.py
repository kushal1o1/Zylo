# Generated by Django 5.0.3 on 2024-11-06 14:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0013_highlight'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SectionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('link', models.URLField()),
                ('pic', models.ImageField(blank=True, null=True, upload_to='section_images/')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_data', to='portfolios.section')),
            ],
        ),
    ]
