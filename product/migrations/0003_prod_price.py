# Generated by Django 4.2.3 on 2024-04-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_prod_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='price',
            field=models.IntegerField(default=110),
        ),
    ]
