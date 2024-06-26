from django.db import models
from config import settings


class Module(models.Model):
    number = models.PositiveIntegerField(verbose_name="Порядковый номер")
    name = models.CharField(max_length=150, verbose_name="Название модуля")
    description = models.TextField(verbose_name="Описание модуля")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"
