# Generated by Django 3.2.4 on 2021-06-24 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_chronicle_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='datetime',
            field=models.DateTimeField(),
        ),
    ]
