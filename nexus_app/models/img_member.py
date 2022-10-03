from django.db import models
from django.contrib.auth.models import AbstractUser

class ImgMember(AbstractUser):
    name = models.CharField(max_length=80, null=True)
    branch = models.CharField(max_length=50, null=True)
    year = models.SmallIntegerField(null=True)
    enrolment_number = models.IntegerField(unique=True, null=True)
    image = models.CharField(max_length=400, null=True, blank=True) 
    # img field

    def __str__(self) -> str:
        return self.username
        