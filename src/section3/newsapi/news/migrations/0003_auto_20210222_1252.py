# Generated by Django 3.1.6 on 2021-02-22 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210222_1243'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jornalist',
            new_name='Journalist',
        ),
    ]