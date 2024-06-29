from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from module.models import Module
from module.validators import validate_youtube


class ModuleSerializer(ModelSerializer):
    video_url = serializers.URLField(validators=[validate_youtube], read_only=True)

    class Meta:
        model = Module
        fields = "__all__"
