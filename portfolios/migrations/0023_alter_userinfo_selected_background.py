# Generated by Django 5.1.1 on 2024-11-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0022_alter_userinfo_selected_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='selected_background',
            field=models.CharField(default='bg0', max_length=6),
        ),
    ]
