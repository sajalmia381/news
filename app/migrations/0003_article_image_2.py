# Generated by Django 2.0.3 on 2018-05-11 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_2',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
