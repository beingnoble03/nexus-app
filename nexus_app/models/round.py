from django.db import models
from .season import Season

class Round(models.Model):
    round_type_choices = [
        ('I', "Interview"),
        ('T', "Test")
    ]
    
    round_name = models.CharField(max_length=50)
    round_type = models.CharField(max_length=1, choices=round_type_choices)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=False,
    related_name="rounds", related_query_name="round")

    def __str__(self) -> str:
        return self.round_name + ' (' + self.round_type + ')'