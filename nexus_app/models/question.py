from django.db import models
from .section import Section
from .img_member import ImgMember

class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    maximum_marks = models.IntegerField()
    assignee = models.ManyToManyField(ImgMember, blank = True)