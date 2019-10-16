# Generated by Django 2.2.6 on 2019-10-16 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0011_auto_20191016_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runner',
            name='department',
        ),
        migrations.AddField(
            model_name='runner',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='competition.University'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
