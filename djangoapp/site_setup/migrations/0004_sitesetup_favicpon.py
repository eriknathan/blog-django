# Generated by Django 4.2.5 on 2023-09-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0003_menulink_site_setup'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='favicpon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m'),
        ),
    ]
