"""
Database Models.
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    """ Manager for userss. """

    def create_user(self, email, password, **extra_fields):
        """ Create, save and return a new user. """

        if not email:
            raise ValueError('User must be valid')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User en el sistema"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    objects = UserManager()  
    USERNAME_FIELD = 'email'
