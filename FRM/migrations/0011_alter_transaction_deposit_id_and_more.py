# Generated by Django 5.0.9 on 2024-09-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRM', '0010_alter_transaction_datetime_local_txn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='deposit_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='product_indicator',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='settlement_amount',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='total_txn_amount',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='txn_sub_code',
            field=models.CharField(max_length=255),
        ),
    ]