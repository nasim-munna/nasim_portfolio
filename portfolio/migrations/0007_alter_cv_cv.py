# Generated by Django 3.2.9 on 2021-12-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='cv',
            field=models.FileField(blank=True, upload_to='cv/'),
        ),
    ]