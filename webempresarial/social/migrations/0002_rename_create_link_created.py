# Generated by Django 5.1 on 2024-08-24 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='create',
            new_name='created',
        ),
    ]
