# Generated by Django 3.0.2 on 2020-01-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoHub', '0005_auto_20200121_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='cover2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='seller',
            name='working_brand',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
