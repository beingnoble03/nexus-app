from django.db import models
from .applicant import Applicant
from .question import Question

class Score(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    obtained_marks = models.IntegerField(verbose_name="Marks")
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100)