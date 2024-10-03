# Generated by Django 5.1 on 2024-09-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRM', '0005_fraudtransactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fraudtransactions',
            name='ACQ_BIN',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='ACQ_COUNTRY',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='DATELOGGED',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='DATETIME_LOCAL_TXN',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='MERCH_CAT',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='MODEL_SCORE',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='POS_ENTRY_MODE',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='RRN',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='RULE_SCORE',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='SETTLEMENT_AMOUNT',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='TOTAL_TXN_AMOUNT',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='TXN_AMOUNT',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='fraudtransactions',
            name='last_4_digits',
            field=models.IntegerField(),
        ),
    ]