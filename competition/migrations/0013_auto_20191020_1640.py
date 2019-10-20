# Generated by Django 2.2.6 on 2019-10-20 14:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0012_auto_20191016_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_limit', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='LapTime',
        ),
        migrations.AddField(
            model_name='group',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='runner',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='competition.Group'),
        ),
        migrations.AlterField(
            model_name='runner',
            name='identification',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9]{8}$', 'This is not a valid university identification number.')]),
        ),
        migrations.AddField(
            model_name='groupscore',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='competition.Group'),
        ),
    ]