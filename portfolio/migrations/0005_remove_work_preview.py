# Generated by Django 3.2.9 on 2021-12-02 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20211202_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='preview',
        ),
    ]
