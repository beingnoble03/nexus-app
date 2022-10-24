from django.db import models
from .round import Round

class Applicant(models.Model):
    role_choices = [
        ('dev', "Developer"),
        ('des', "Designer")
    ]
    status_choices = [
        ('Evaluated', "Evaluated"),
        ('Not Evaluated', "Not Evaluated"),
        ('Called', "Called"),
        ('Not Called', "Not Called")
    ]

    name = models.CharField(max_length=50)
    enrolment_number = models.BigIntegerField(null=False, unique=True)
    branch = models.CharField(max_length=50)
    mobile = models.CharField(max_length=13)
    status = models.CharField(max_length=50, null=True,
    choices=status_choices)
    stage = models.ForeignKey(Round, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=3, choices=role_choices)
    email = models.EmailField()
    year = models.IntegerField()
    round = models.ManyToManyField(Round, related_name="applicants",
    related_query_name="applicant", blank=True)
    
    def __str__(self) -> str:
        return self.name + ' (' + str(self.enrolment_number) + ')'