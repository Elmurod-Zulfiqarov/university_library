# Generated by Django 3.2.6 on 2021-10-07 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_bookrecord_returned_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_records', to='library.user'),
        ),
    ]
