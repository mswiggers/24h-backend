# Generated by Django 2.2 on 2019-04-26 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_happyhour_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runner',
            name='identification',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^[rsu][0-9]{7}$', 'This is not a valid university identification number.')]),
        ),
    ]