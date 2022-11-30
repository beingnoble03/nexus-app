from django.db import models
from .round import Round

class Test(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE,
    related_name="tests")
    title = models.CharField(max_length=50, unique=False)