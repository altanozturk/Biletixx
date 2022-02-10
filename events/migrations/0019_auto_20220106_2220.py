# Generated by Django 3.1.4 on 2022-01-06 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0018_auto_20220101_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='max_sellable_tickets',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='price',
        ),
        migrations.AddField(
            model_name='event',
            name='max_sellable_tickets',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]