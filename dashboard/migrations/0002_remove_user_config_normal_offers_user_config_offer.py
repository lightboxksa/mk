# Generated by Django 4.0 on 2022-03-15 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0010_alter_offers_product_id'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_config',
            name='normal_offers',
        ),
        migrations.AddField(
            model_name='user_config',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offers.offers'),
        ),
    ]
