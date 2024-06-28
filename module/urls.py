from django.urls import path

from module.apps import ModuleConfig
from module.views import (
    ModuleCreateApiView,
    ModuleListApiView,
    ModuleRetrieveApiView,
    ModuleDestroyApiView,
    ModuleUpdateApiView,
)

app_name = ModuleConfig.name


urlpatterns = [
    path("", ModuleListApiView.as_view(), name="module-list"),
    path("<int:pk>/", ModuleRetrieveApiView.as_view(), name="module-retrieve"),
    path("create/", ModuleCreateApiView.as_view(), name="module-create"),
    path("delete/<int:pk>/", ModuleDestroyApiView.as_view(), name="module-delete"),
    path("update/<int:pk>/", ModuleUpdateApiView.as_view(), name="module-update"),
]
