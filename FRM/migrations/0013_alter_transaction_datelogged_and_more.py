# Generated by Django 5.0.9 on 2024-09-17 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRM', '0012_alter_transaction_rrn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='datelogged',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='datetime_local_txn',
            field=models.DateTimeField(),
        ),
    ]
