from django.db import models
from django.contrib.auth.models import User

class UsersAuth(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.SmallIntegerField(default=0)
    email = models.EmailField(unique=True, default='SkillFactoryTest@yandex.ru')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.SmallIntegerField(default=0)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
