# Generated by Django 2.2 on 2019-07-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0003_auto_20190426_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lap',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='lap',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]