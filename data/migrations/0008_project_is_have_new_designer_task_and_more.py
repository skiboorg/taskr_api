# Generated by Django 4.0.1 on 2022-01-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_projectlink_link_alter_projectlink_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_have_new_designer_task',
            field=models.BooleanField(default=False, verbose_name='Есть новые задачи дизайнеру'),
        ),
        migrations.AddField(
            model_name='project',
            name='is_have_new_proger_task',
            field=models.BooleanField(default=False, verbose_name='Есть новые задачи прогеру'),
        ),
        migrations.AddField(
            model_name='project',
            name='new_tasks_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Цвет, например red, blue, green'),
        ),
        migrations.AddField(
            model_name='task',
            name='is_designer_task',
            field=models.BooleanField(default=False, verbose_name='Задача дизайнеру'),
        ),
        migrations.AddField(
            model_name='task',
            name='is_new',
            field=models.BooleanField(default=True, verbose_name='Новая'),
        ),
        migrations.AddField(
            model_name='task',
            name='is_proger_task',
            field=models.BooleanField(default=False, verbose_name='Задача прогеру'),
        ),
    ]