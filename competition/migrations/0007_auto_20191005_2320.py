# Generated by Django 2.2.6 on 2019-10-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0006_laptime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lap',
            name='duration',
            field=models.IntegerField(null=True),
        ),
    ]