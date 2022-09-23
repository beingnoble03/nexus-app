from django.db import models
from .img_member import ImgMember

class Panel(models.Model):
    place = models.CharField(max_length=100)
    available = models.BooleanField()
    status = models.CharField(max_length=50)
    members = models.ForeignKey(ImgMember, on_delete=models.CASCADE)