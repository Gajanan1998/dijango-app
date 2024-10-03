# Generated by Django 5.0.9 on 2024-09-24 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRM', '0013_alter_transaction_datelogged_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruleName', models.CharField(max_length=255, unique=True)),
                ('rule_details', models.CharField(max_length=255)),
                ('rule_desc', models.TextField(max_length=1000)),
                ('rule_status', models.CharField(choices=[('Activate', 'Activate'), ('Deactivate', 'Deactivate')], default='Activate', max_length=10)),
                ('rule_created_date', models.DateTimeField()),
                ('rule_expiry_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Rule',
            },
        ),
    ]
