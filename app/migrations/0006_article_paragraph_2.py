# Generated by Django 2.0.3 on 2018-05-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180511_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='paragraph_2',
            field=models.TextField(blank=True),
        ),
    ]