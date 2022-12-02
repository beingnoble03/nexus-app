from .applicant import Applicant
from .img_member import ImgMember
from .interview import Interview
from .interview_section import InterviewSection
from .panel import Panel
from .question import Question
from .round import Round
from .score import Score
from .season import Season
from .section import Section
from .section_marks import SectionMarks
from .test import Test
from .message import Message
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    if not instance.image:
        instance.image = "https://cdn-icons-png.flaticon.com/512/149/149071.png"
        instance.save()