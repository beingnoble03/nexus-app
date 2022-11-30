from django.urls import re_path
from djangochannelsrestframework.consumers import view_as_consumer
from .views import InterviewViewSet
from .consumers import InterviewConsumer

websocket_urlpatterns = [
    # re_path(r'^interviews/$', view_as_consumer(InterviewViewSet.as_view()))
    # re_path(r'^ws/interviews/$', view_as_consumer(InterviewViewSet.as_view({
    #     "get": "list",
    #     "post": "create",
    #     "patch": "update",
    # }))),
    re_path(r'ws/interviews/(?P<round_id>[^/]+)/$', InterviewConsumer.as_asgi()),
]