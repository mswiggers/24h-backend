# Generated by Django 2.2.6 on 2019-10-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0005_auto_20191003_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='LapTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_limit', models.DurationField()),
                ('score', models.IntegerField()),
            ],
        ),
    ]
