# Generated by Django 4.0 on 2022-03-15 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0010_alter_offers_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_process',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
