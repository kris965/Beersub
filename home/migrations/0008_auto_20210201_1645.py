# Generated by Django 3.1.5 on 2021-02-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210201_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('Y', 'yellow'), ('DK', 'dark-yellow'), ('LO', 'ligh-torange'), ('A', 'amber'), ('LB', 'light-brown'), ('B', 'brown'), ('DB', 'dark-brown'), ('BK', 'black')], max_length=2),
        ),
    ]