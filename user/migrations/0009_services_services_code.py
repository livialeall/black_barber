# Generated by Django 5.0 on 2023-12-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_services_services_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='services_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]