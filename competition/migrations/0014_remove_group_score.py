# Generated by Django 2.2.6 on 2019-10-20 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0013_auto_20191020_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='score',
        ),
    ]
