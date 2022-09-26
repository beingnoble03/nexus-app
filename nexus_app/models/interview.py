from django.db import models
from .applicant import Applicant
from .panel import Panel
from .round import Round

class Interview(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE, null = True)
    time_assigned = models.DateTimeField(null = True)
    time_entered = models.DateTimeField(null = True)
    completed = models.BooleanField(default=False)
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name="interviews")
    remarks = models.CharField(max_length=100)