# Generated by Django 3.0.6 on 2020-06-16 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20200608_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='Type',
            new_name='_type',
        ),
    ]
