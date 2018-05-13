# Generated by Django 2.0.3 on 2018-05-12 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_article_paragraph_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Article')),
            ],
        ),
    ]
