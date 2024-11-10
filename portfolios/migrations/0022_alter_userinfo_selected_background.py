# Generated by Django 5.1.1 on 2024-11-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0021_alter_userinfo_selected_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='selected_background',
            field=models.CharField(choices=[('bg0', 'Default Background'), ('bg1', 'Minimalistic Graph'), ('bg2', 'Big Box Design'), ('bg3', 'Checkerboard Pattern'), ('bg4', 'Dotted Grid'), ('bg5', 'Dotted Background'), ('bg6', 'Large Grid Boxes'), ('bg7', 'Overlay Effect'), ('bg8', 'Test Pattern'), ('bg9', 'Animated Canvas'), ('bg10', 'Animated Circles'), ('bg11', 'Color Circles Animation'), ('bg12', 'Diagonal Stripes Animation'), ('bg13', 'Hexagonal Pattern'), ('bg14', 'Polygonal Shapes'), ('bg15', 'Star Animation'), ('bg16', 'Test Animation'), ('bg17', 'Particles Animation'), ('bg18', 'Wavy Background'), ('bg19', 'Polygon Background')], default='bg0', max_length=6),
        ),
    ]