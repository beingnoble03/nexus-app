from django.db import models
from .interview_section import InterviewSection

class SectionMarks(models.Model):
    obtained_marks = models.IntegerField()
    section = models.ForeignKey(InterviewSection, on_delete=models.CASCADE)