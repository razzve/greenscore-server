# Generated by Django 4.1.1 on 2022-12-05 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statsnyc', '0006_alter_energy_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='energy',
            options={'managed': False},
        ),
    ]