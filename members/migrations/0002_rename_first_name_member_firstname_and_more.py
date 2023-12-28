# Generated by Django 5.0 on 2023-12-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='member',
            name='joining_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]