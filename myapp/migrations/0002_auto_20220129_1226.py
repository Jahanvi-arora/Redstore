# Generated by Django 3.2.4 on 2022-01-29 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Dealer',
        ),
        migrations.RenameModel(
            old_name='Book',
            new_name='Product',
        ),
    ]
