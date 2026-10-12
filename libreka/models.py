from django.db import models


class User(models.Model):
    username = models.CharField(max_length=80, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=80)

    def __str__(self) -> str:
        return self.username
