from django.db import models
from nexus_app.models import Interview
from .interview_section import InterviewSection

class SectionMarks(models.Model):
    obtained_marks = models.IntegerField()
    section = models.ForeignKey(InterviewSection, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE, related_name="section_marks_set", null=True)