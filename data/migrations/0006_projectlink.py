# Generated by Django 4.0.1 on 2022-01-19 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_task_options_taskfile_name_alter_taskfile_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='Название')),
                ('link', models.TextField(blank=True, editable=False, null=True, verbose_name='ссылка')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='data.project')),
            ],
        ),
    ]