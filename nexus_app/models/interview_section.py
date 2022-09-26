from django.db import models
from .round import Round

class InterviewSection(models.Model):
    title = models.CharField(max_length=50)
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name="interview_sections")
    maximum_marks = models.IntegerField()