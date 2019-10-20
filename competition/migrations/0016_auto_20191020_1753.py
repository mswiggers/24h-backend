# Generated by Django 2.2.6 on 2019-10-20 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0015_auto_20191020_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='happyhour',
            old_name='bonus',
            new_name='multiplier',
        ),
        migrations.AlterField(
            model_name='groupscore',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='competition.Group'),
        ),
    ]
