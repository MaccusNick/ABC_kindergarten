# Generated by Django 3.0.5 on 2020-05-28 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200528_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]