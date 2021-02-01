# Generated by Django 3.1.5 on 2021-02-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210201_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.AddField(
            model_name='item',
            name='percentage',
            field=models.CharField(default='name', max_length=2),
            preserve_default=False,
        ),
    ]
