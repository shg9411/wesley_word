# Generated by Django 3.0.6 on 2020-06-22 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0008_word_theme'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['theme', 'word']},
        ),
    ]