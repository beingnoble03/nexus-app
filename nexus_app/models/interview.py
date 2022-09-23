from django.db import models
from .applicant import Applicant
from .panel import Panel
from .round import Round
from .section_marks import SectionMarks

class Interview(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    time_assigned = models.DateTimeField(null = True)
    time_entered = models.DateTimeField(null = True)
    completed = models.BooleanField()
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name="interviews")
    section_marks = models.ForeignKey(SectionMarks, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100)