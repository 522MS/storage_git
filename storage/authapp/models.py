from django.db import models

from django.contrib.auth.models import AbstractUser


class StorageUser(AbstractUser):
    age = models.PositiveIntegerField(
        verbose_name='возраст',
        default=18,
    )
