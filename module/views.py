from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from module.models import Module
from module.serializers import ModuleSerializer


class ModuleCreateApiView(CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleListApiView(ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleRetrieveApiView(RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleUpdateApiView(UpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class ModuleDestroyApiView(DestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
