from email import message
from django.db import models
from .img_member import ImgMember
from .interview import Interview

class Message(models.Model):
    message = models.CharField(max_length=255)
    author = models.ForeignKey(ImgMember, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - in {self.interview}"

    class Meta:
        ordering = ["-timestamp", ]