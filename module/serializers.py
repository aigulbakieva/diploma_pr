from rest_framework.serializers import ModelSerializer

from module.models import Module


class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"
