from django.db import models
from config import settings


class Module(models.Model):
    number = models.PositiveIntegerField(verbose_name="Порядковый номер")
    name = models.CharField(max_length=150, verbose_name="Название модуля")
    description = models.TextField(verbose_name="Описание модуля")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        blank=True,
        null=True,
    )
    preview = models.ImageField(
        upload_to="module/previews", verbose_name="Картинка", blank=True, null=True
    )
    video_url = models.URLField(verbose_name="ссылка на видео", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"


class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="subscription",
    )
    module = models.ForeignKey(
        Module,
        null=True,
        blank=True,
        verbose_name="Модуль",
        on_delete=models.CASCADE,
        related_name="subscription",
    )

    def __str__(self):
        return f"{self.user} - {self.module}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
