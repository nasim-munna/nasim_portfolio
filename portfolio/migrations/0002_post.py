# Generated by Django 3.2.9 on 2021-12-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='blog/')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
