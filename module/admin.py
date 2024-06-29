from django.contrib import admin

from module.models import Module, Subscription


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "owner",
        "number",
        "name",
        "description",
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "module",
    )
