# Generated by Django 4.0 on 2022-03-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_page_controler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page_controler',
            name='hover_title',
            field=models.CharField(max_length=100),
        ),
    ]
