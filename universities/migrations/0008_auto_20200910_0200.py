# Generated by Django 3.1 on 2020-09-10 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0007_auto_20200910_0158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nearbyrestaurant',
            old_name='restaurant',
            new_name='university',
        ),
    ]
