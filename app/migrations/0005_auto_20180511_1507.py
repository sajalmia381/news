# Generated by Django 2.0.3 on 2018-05-11 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180511_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_2',
            field=models.FileField(blank=True, default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
