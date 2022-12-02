from django.urls import re_path
from .consumers import InterviewConsumer, MessageConsumer

websocket_urlpatterns = [
    re_path(r'ws/interviews/(?P<round_id>[^/]+)/$', InterviewConsumer.as_asgi()),
    re_path(r'ws/messages/(?P<interview_id>[^/]+)/$', MessageConsumer.as_asgi()),
]