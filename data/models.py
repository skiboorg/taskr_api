from django.db import models
from pytils.translit import slugify
import uuid
from django.db.models.signals import post_save

class Tag(models.Model):
    name = models.CharField('Название', max_length=100, blank=True, null=True)
    color = models.CharField('Цвет, например red, blue, green', max_length=20, blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

class ProjectStatus(models.Model):
    name = models.CharField('Название', max_length=100, blank=False, null=True)
    icon = models.ImageField('Иконка', upload_to='icons/', blank=False, null=True)

class Project(models.Model):
    name = models.CharField('Название', max_length=100, blank=True, null=True)
    name_slug = models.CharField('Название', max_length=100, blank=True, null=True,editable=False)
    statuses = models.ManyToManyField(ProjectStatus, blank=True)
    image_mob = models.ImageField('Баннер', upload_to='project/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    new_tasks_count = models.IntegerField(default=0)
    is_have_new_proger_task = models.BooleanField('Есть новые задачи прогеру', default=False)
    is_have_new_designer_task = models.BooleanField('Есть новые задачи дизайнеру', default=False)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        print('sdf')
        task_for_proger = False
        task_for_designer = False
        for task in self.task_set.all():
            if task.is_proger_task and task.is_new:
                task_for_proger = True

            if task.is_designer_task and task.is_new:
                task_for_designer = True

        self.is_have_new_designer_task = task_for_designer
        self.is_have_new_proger_task = task_for_proger
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

class ProjectLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='links')
    name = models.CharField('Название', max_length=100, blank=True, null=True)
    link = models.TextField('ссылка',  blank=True, null=True)




class Column(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name='columns')
    name = models.CharField('Название', max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Task(models.Model):
    order_num = models.CharField(blank=True,null=True, max_length=10)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, null=True, blank=True, related_name='tasks')
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField('Название', max_length=100, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    is_done = models.BooleanField(default=False)
    dead_line = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_proger_task = models.BooleanField('Задача прогеру', default=False)
    is_designer_task = models.BooleanField('Задача дизайнеру', default=False)
    is_new = models.BooleanField('Новая', default=True)

    def __str__(self):
        return f'{self.order_num} - {self.name}'

    def save(self, *args, **kwargs):
        if not self.order_num:
            total_task_in_column = self.column.tasks.count()
            self.order_num = f'c{self.column.id}t{total_task_in_column+1}'


        super().save(*args, **kwargs)

    class Meta:
        ordering = ('order_num',)

class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True, related_name='files')
    name = models.CharField('Название', max_length=100, blank=True, null=True)
    file = models.FileField('Файл', upload_to='task/', blank=True, null=True)


class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

def task_post_save(sender, instance, created, **kwargs):
    """Создание всех значений по-умолчанию для нового пользовыателя"""
    instance.project.save()

post_save.connect(task_post_save, sender=Task)