# Generated by Django 4.0.1 on 2022-01-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_designer',
            field=models.BooleanField(default=False, verbose_name='Дизайнер'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_proger',
            field=models.BooleanField(default=False, verbose_name='Прогер'),
        ),
    ]
