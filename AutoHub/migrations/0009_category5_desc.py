# Generated by Django 3.0.2 on 2020-01-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoHub', '0008_auto_20200124_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='category5',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
