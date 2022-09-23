from django.db import models

class Season(models.Model):
    season_role_choices = [
        ('dev', "Developer"),
        ('des', "Designer")
    ]
    
    year = models.IntegerField(null=False)
    role = models.CharField(max_length=3, choices=season_role_choices)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=100)
