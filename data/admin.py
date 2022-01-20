from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Column)
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(TaskFile)
admin.site.register(ProjectLink)
admin.site.register(TaskComment)

