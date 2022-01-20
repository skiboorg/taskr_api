from django.urls import path,include
from . import views

urlpatterns = [
    path('tags', views.GetTags.as_view()),
    path('projects', views.GetProjects.as_view()),
    path('project', views.GetProject.as_view()),
    path('add_project_link', views.AddProjectLink.as_view()),
    path('del_project_link', views.DelProjectLink.as_view()),
    path('new_project', views.NewProject.as_view()),
    path('delete_project', views.DeleteProject.as_view()),
    path('add_column', views.AddColumn.as_view()),
    path('delete_column', views.DeleteColumn.as_view()),
    path('edit_column', views.EditColumn.as_view()),

    path('add_task', views.AddTask.as_view()),
    path('add_task_comment', views.AddTaskComment.as_view()),
    path('task_done', views.AddDone.as_view()),
    path('delete_task', views.DeleteTask.as_view()),
    path('move_task_to_col', views.MoveTaskToColumn.as_view()),
    path('reorder_tasks', views.ReorderTasks.as_view()),


]
