from rest_framework.serializers import ModelSerializer
from module.models import Module
from module.validators import YoutubeValidator


class ModuleSerializer(ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"
        validators = [YoutubeValidator(field='video_url'),]

