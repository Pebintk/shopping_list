# Generated by Django 4.2.5 on 2023-09-13 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='print',
            new_name='price',
        ),
    ]
