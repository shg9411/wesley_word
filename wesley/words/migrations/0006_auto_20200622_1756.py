# Generated by Django 3.0.6 on 2020-06-22 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_auto_20200622_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='theme',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='words.Theme'),
        ),
    ]
