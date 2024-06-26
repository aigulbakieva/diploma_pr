from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )
    first_name = models.CharField(
        max_length=50, verbose_name="Имя", help_text="Укажите имя"
    )
    last_name = models.CharField(
        max_length=50, verbose_name="Фамилия", help_text="Укажите фамилию"
    )
    phone = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Номер телефона",
        help_text="Укажите номер телефона",
    )
    photo = models.ImageField(
        upload_to="users/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
