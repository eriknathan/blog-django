# Generated by Django 4.2.5 on 2023-09-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_sitesetup_favicpon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetup',
            name='favicpon',
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m'),
        ),
    ]
