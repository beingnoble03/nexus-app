from django.db import models
from .img_member import ImgMember

class Panel(models.Model):
    status_choices = [
        ('Busy', "Busy"),
        ('Vacant', "Vacant")
    ]
    place = models.CharField(max_length=100)
    available = models.BooleanField()
    status = models.CharField(max_length=50, choices=status_choices)
    members = models.ManyToManyField(ImgMember, blank = True)

    def __str__(self) -> str:
        return self.place