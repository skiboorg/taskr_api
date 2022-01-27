from rest_framework import serializers
from .models import *
from user.serializers import UserSerializer
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatus
        fields = '__all__'

class ProjectLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLink
        fields = '__all__'


class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFile
        fields = '__all__'

class TaskCommentSerializer(serializers.ModelSerializer):
    user=UserSerializer(many=False, read_only=True, required=False)
    class Meta:
        model = TaskComment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=False, read_only=True, required=False)
    files = TaskFileSerializer(many=True, read_only=True, required=False)
    comments = TaskCommentSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Task
        fields = '__all__'

class ColumnSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Column
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    links = ProjectLinkSerializer(many=True, read_only=True, required=False)
    columns = ColumnSerializer(many=True, read_only=True, required=False)
    # statuses = ProjectStatusSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Project
        fields = '__all__'





