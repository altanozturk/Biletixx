# Generated by Django 3.1.4 on 2021-12-16 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('eventtype', models.CharField(choices=[('Concert', 'Concert'), ('StageShow', 'StageShow')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('ticketname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventTicketSell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_sellable_tickets', models.IntegerField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.date')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.ticket_class')),
            ],
        ),
    ]