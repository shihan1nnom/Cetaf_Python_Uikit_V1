# Generated by Django 3.2.5 on 2021-07-15 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cetaf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sede',
            options={'permissions': (('gestion_sede', 'Gestionar sedes'),)},
        ),
    ]
