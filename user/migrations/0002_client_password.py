# Generated by Django 5.0 on 2023-12-18 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default='x', max_length=50, verbose_name='Senha'),
        ),
    ]