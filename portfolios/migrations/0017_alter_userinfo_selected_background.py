# Generated by Django 5.0.3 on 2024-11-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0016_remove_userinfo_highlight_thumbnail_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='selected_background',
            field=models.CharField(choices=[('bg1', 'Minimalistic Graph'), ('bg2', 'Big Box Design'), ('bg3', 'Checkerboard Pattern'), ('bg4', 'Dotted Grid'), ('bg5', 'Dotted Background'), ('bg6', 'Large Grid Boxes'), ('bg7', 'Overlay Effect'), ('bg8', 'Test Pattern'), ('bg9', 'Animated Canvas'), ('bg10', 'Animated Circles'), ('bg11', 'Color Circles Animation'), ('bg12', 'Diagonal Stripes Animation'), ('bg13', 'Hexagonal Pattern'), ('bg14', 'Polygonal Shapes'), ('bg15', 'Star Animation'), ('bg16', 'Test Animation'), ('bg17', 'Particles Animation')], default='bg1', max_length=6),
        ),
    ]