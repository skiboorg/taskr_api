# Generated by Django 4.0.1 on 2022-01-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_remove_task_uid_task_order_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('order_num',)},
        ),
        migrations.AddField(
            model_name='taskfile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='taskfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='task/', verbose_name='Файл'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
