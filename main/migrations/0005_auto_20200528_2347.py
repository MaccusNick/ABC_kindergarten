# Generated by Django 3.0.5 on 2020-05-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200528_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherschedule',
            name='StartTime',
            field=models.DateTimeField(),
        ),
    ]