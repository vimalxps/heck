# Generated by Django 4.2.3 on 2023-07-31 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='desc',
            new_name='description',
        ),
    ]
