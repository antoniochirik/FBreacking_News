from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):

    def _create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError('User must have a username.')
        if password is None:
            raise TypeError('User must have a password.')
        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            username=username,
            password=password,
            **extra_fields
        )

    # def create_superuser(self, username, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     return self._create_user(
    #         username=username,
    #         password=password,
    #         **extra_fields
    #     )


class User(AbstractBaseUser):
    username = models.CharField(
        db_index=True,
        max_length=200,
        unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username
