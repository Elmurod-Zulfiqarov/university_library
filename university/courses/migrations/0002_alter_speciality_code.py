# Generated by Django 3.2.6 on 2021-08-26 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='code',
            field=models.IntegerField(),
        ),
    ]
