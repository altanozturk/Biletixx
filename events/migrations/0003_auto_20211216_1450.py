# Generated by Django 3.1.4 on 2021-12-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20211216_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.CharField(choices=[('Today', 'Today'), ('NextWeek', 'NextWeek')], max_length=200, null=True),
        ),
    ]
