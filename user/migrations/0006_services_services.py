# Generated by Django 5.0 on 2023-12-19 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_appointments_delete_appointment_delete_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='services',
            field=models.CharField(blank=True, choices=[('Corte Adulto', 'Corte Adulto'), ('Corte Infantil', 'Corte Infantil'), ('Barba Completa', 'Barba Completa')], max_length=100, null=True),
        ),
    ]