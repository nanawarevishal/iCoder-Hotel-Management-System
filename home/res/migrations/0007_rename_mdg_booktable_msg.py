# Generated by Django 4.1 on 2022-08-15 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0006_booktable_mdg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booktable',
            old_name='mdg',
            new_name='msg',
        ),
    ]
