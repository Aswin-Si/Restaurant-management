# Generated by Django 4.2.6 on 2023-11-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(blank=True, max_length=100, null=True)),
                ('Time', models.TimeField(blank=True, null=True)),
                ('Person', models.CharField(blank=True, max_length=100, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
