# Generated by Django 4.2.11 on 2024-06-07 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_contract_monthtomoney'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='advance_payment',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
    ]
