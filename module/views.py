from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from module.models import Module, Subscription
from module.paginations import CustomPagination
from module.serializers import ModuleSerializer
from users.permissions import IsOwner, IsModerator


class ModuleCreateApiView(CreateAPIView):
    """Класс для создания модуля."""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        module = serializer.save()
        module.owner = self.request.user
        module.save()


class ModuleListApiView(ListAPIView):
    """Класс для вывода списка модулей."""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    pagination_class = CustomPagination


class ModuleRetrieveApiView(RetrieveAPIView):
    """Класс для подробной информации конкретного модуля."""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (IsOwner | IsModerator, IsAuthenticated)


class ModuleUpdateApiView(UpdateAPIView):
    """Класс для редактирования модуля."""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (IsOwner | IsModerator, IsAuthenticated)


class ModuleDestroyApiView(DestroyAPIView):
    """Класс для удаления модуля."""

    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (IsOwner | IsModerator, IsAuthenticated)


class SubscriptionApiView(APIView):
    """Подписка на модуль."""

    def post(self, *args, **kwargs):
        user = self.request.user
        module_id = self.request.data.get("module")
        module_item = get_object_or_404(Module, pk=module_id)

        subs_item = Subscription.objects.filter(user=user, course=module_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=user, course=module_item)
            message = "Подписка добавлена"
        return Response({"message": message}, status=status.HTTP_200_OK)
