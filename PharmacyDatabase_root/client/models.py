from django.db import models
from django.contrib.auth.models import User


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=32, blank=True)
    lastname = models.CharField(max_length=32, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    email = models.CharField(max_length=32, blank=True)
    address = models.CharField(max_length=64, blank=False)
    birth_date = models.DateField()

    image = models.ImageField(upload_to='uploads/profile_pics', blank=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
