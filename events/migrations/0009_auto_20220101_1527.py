# Generated by Django 3.1.4 on 2022-01-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20220101_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='hour',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='eventtype',
            field=models.CharField(choices=[('Concert', 'Concert'), ('StageShow', 'StageShow'), ('Movie', 'Movie'), ('Theatre', 'Theatre'), ('Sport', 'Sport'), ('Musical', 'Musical')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.CharField(choices=[('Istanbul', 'Istanbul'), ('Ankara', 'Ankara'), ('İzmir', 'İzmir'), ('Eskişehir', 'Eskişehir'), ('Edirne', 'Edirne'), ('Antalya', 'Antalya')], max_length=200, null=True),
        ),
    ]
