# Generated by Django 5.1 on 2024-09-05 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FRM', '0002_alter_credentials_email_alter_credentials_username'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='credentials',
            table='Credentials',
        ),
    ]
