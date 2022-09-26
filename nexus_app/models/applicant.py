from django.db import models
from .round import Round

class Applicant(models.Model):
    name = models.CharField(max_length=50)
    enrollment_number = models.BigIntegerField(null=False, unique=True)
    branch = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)
    status = models.CharField(max_length=50, null = True) 
    stage = models.CharField(max_length=50, null = True) # foriegn key round
    role = models.CharField(max_length=50)
    email = models.EmailField()
    year = models.IntegerField()
    round = models.ManyToManyField(Round, related_name="applicants", related_query_name="applicant", blank = True)