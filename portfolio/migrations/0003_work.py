# Generated by Django 3.2.9 on 2021-12-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='blog/')),
                ('url', models.URLField()),
            ],
        ),
    ]