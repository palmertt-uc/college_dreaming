# Generated by Django 3.1.2 on 2020-11-13 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('universities', '0024_auto_20201113_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutions',
            name='favorite',
            field=models.ManyToManyField(blank=True, default=None, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
