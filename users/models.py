from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# user = CustomUser(email='email')
# user.set_password('password')
# user.save()
