from django.db import models
from django.contrib.auth.models import AbstractUser

class ImgMember(AbstractUser):
    branch = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=50, null=True) # remove
    year = models.SmallIntegerField(null=True)
    enrollment_number = models.IntegerField(unique=True, null=True)

    def __str__(self) -> str:
        return self.username