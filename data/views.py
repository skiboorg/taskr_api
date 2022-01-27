from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import *
from .serializers import *
import json


class GetProjects(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class GetTags(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class GetStatuses(generics.ListAPIView):
    serializer_class = ProjectStatusSerializer
    queryset = ProjectStatus.objects.all()


class GetProject(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer

    def get_object(self):
        return Project.objects.get(name_slug=self.request.query_params.get('name_slug'))


class NewProject(APIView):
    def post(self,request):
        Project.objects.create(name=request.data.get('name'),image_mob=request.FILES.getlist('image')[0])
        return Response(status=200)

class DelProjectLink(APIView):
    def post(self,request):
        ProjectLink.objects.get(id=request.data.get('id')).delete()
        return Response(status=200)

class AddProjectLink(APIView):
    def post(self,request):
        print(request.data)
        ProjectLink.objects.create(
            project_id=request.data.get('id'),
            name=request.data.get('name'),
            link=request.data.get('link'),
        )
        return Response(status=200)


class DeleteProject(APIView):
    def post(self,request):
        Project.objects.get(id=request.data.get('id')).delete()
        return Response(status=200)

class ProjectStatus(APIView):
    def post(self,request):
        print(request.data)
        project = Project.objects.get(id=request.data.get('id'))
        project.statuses.clear()
        for i in request.data.get('statuses'):
            project.statuses.add(i)

        return Response(status=200)




class AddColumn(APIView):
    def post(self,request):
        Column.objects.create(project_id=request.data.get('p_id'),name='Новая колонка')
        return Response(status=200)


class DeleteColumn(APIView):
    def post(self,request):
        Column.objects.get(id=request.data.get('c_id')).delete()
        return Response(status=200)

class EditColumn(APIView):
    def post(self,request):
        column = Column.objects.get(id=request.data.get('c_id'))
        column.name = request.data.get('name')
        column.save()
        return Response(status=200)


class AddTask(APIView):
    def post(self,request):
        print(request.data)
        project_id = request.data.get('p_id')
        column_id = request.data.get('c_id')
        data = json.loads(request.data.get('data'))
        file_names = request.data.getlist('file_names')

        dead_line_raw = data['dead_line'].replace('Январь','01'). \
            replace('Февраль','02'). \
            replace('Март','03'). \
            replace('Апрель','04'). \
            replace('Май','05'). \
            replace('Июнь','06'). \
            replace('Июль','07'). \
            replace('Август','08'). \
            replace('Сентябрь','09'). \
            replace('Октябрь','10'). \
            replace('Ноябрь','11'). \
            replace('Декабрь','12').split(' ')

        dead_line = f'{dead_line_raw[2]}-{dead_line_raw[1]}-{dead_line_raw[0]}'
        task = Task.objects.create(
            project_id=project_id,
            column_id=column_id,
            name=data['name'],
            dead_line=dead_line,
            tag_id=data['tag']['id'],
            description=data['description'],
            is_proger_task=data['is_proger'],
            is_designer_task=data['is_designer'],
        )

        for i,name in enumerate(file_names):
            print(i)
            print(name)
            print(request.FILES.getlist('files')[i])
            TaskFile.objects.create(task=task,name=name,file=request.FILES.getlist('files')[i])



        return Response(status=200)


class MoveTaskToColumn(APIView):
    def post(self,request):
        print(request.data)
        to_column_id=request.data.get('to_column_id')
        task_id=request.data.get('task_id')
        task = Task.objects.get(id=task_id)
        to_column = Column.objects.get(id=to_column_id)
        task.column = to_column
        total_task_in_column = to_column.tasks.count()
        task.order_num = f'c{task.column.id}t{total_task_in_column + 1}'
        task.save()

        return Response(status=200)


class ReorderTasks(APIView):
    def post(self,request):
        print(request.data)
        for task_obj in request.data.get('tasks'):
            task = Task.objects.get(id=task_obj['id'])
            task.order_num = task_obj['order']
            task.save()

        return Response(status=200)


class DeleteTask(APIView):
    def post(self,request):
        Task.objects.get(id=request.data.get('id')).delete()
        return Response(status=200)

class TaskView(APIView):
    def post(self,request):
        task = Task.objects.get(id=request.data.get('id'))
        task.is_new = False
        task.save()
        return Response(status=200)

class AddDone(APIView):
    def post(self,request):
        task = Task.objects.get(id=request.data.get('id'))
        task.is_done = True
        task.save()
        return Response(status=200)

class AddTaskComment(APIView):
    def post(self,request):
        TaskComment.objects.create(
            task_id=request.data.get('task_id'),
            user=request.user,
            text=request.data.get('text')
        )

        return Response(status=200)