# from .models import Interview
# from .api.serializers.interview import InterviewSerializer
# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework.mixins import ListModelMixin, PatchModelMixin, CreateModelMixin
# from djangochannelsrestframework.observer import model_observer
# from djangochannelsrestframework import permissions
# from djangochannelsrestframework.decorators import action
# from rest_framework import status
# from urllib.parse import parse_qs


# class InterviewConsumer(
#     GenericAsyncAPIConsumer,
#     ListModelMixin,
#     PatchModelMixin,
#     CreateModelMixin,
# ):
#     queryset = Interview.objects.all()
#     serializer_class = InterviewSerializer

#     async def connect(self, **kwargs):
#         query_params = parse_qs(self.scope["query_string"].decode())
#         await super().connect()

#     @model_observer(Interview)
#     async def model_change(self, message, observer=None, **kwargs):
#         await self.send_json(message)

#     @model_change.serializer
#     def model_serialize(self, instance, action, **kwargs):
#         return dict(data = InterviewSerializer(instance=instance).data, action = action.value)

#     @action()
#     def list_interviews_for_round(self, request_id, round_id, **kwargs):
#         queryset = Interview.objects.filter(round__id = round_id)
#         return InterviewSerializer(instance=queryset, many=True).data, status.HTTP_200_OK

from channels.generic.websocket import WebsocketConsumer
from nexus_app.models import Panel
from nexus_app.models import Interview
from nexus_app.api.serializers.interview import InterviewSerializer
import json
from asgiref.sync import async_to_sync

class InterviewConsumer(WebsocketConsumer):
    def send_interviews(self):
        queryset = Interview.objects.filter(round__id=self.round_id)
        serializer = InterviewSerializer(instance=queryset, many=True)
        async_to_sync(self.channel_layer.group_send)(
            self.round_group_name, {"type": "interview", "interviews": serializer.data, "action_type": "list"}
        )

    def update_interview(self, data):
        interview = Interview.objects.get(id=data["interview"])
        if data["panel"]:
            panel = Panel.objects.get(id=data["panel"])
            interview.panel = panel
        else:
            interview.panel = None
        interview.time_assigned = data["time_assigned"]
        interview.time_entered = data["time_entered"]
        interview.completed = data["completed"]
        interview.save()
        serializer = InterviewSerializer(instance=interview)
        async_to_sync(self.channel_layer.group_send)(
            self.round_group_name, {"type": "interview", "interviews": serializer.data, "action_type": "updated_interview"}
        )

    def fetch_interview(self, data):
        interview = Interview.objects.get(id=data["interview"])
        serializer = InterviewSerializer(instance=interview)
        async_to_sync(self.channel_layer.group_send)(
            self.round_group_name, {"type": "interview", "interviews": serializer.data, "action_type": "updated_interview"}
        )

    def interview(self, event):
        interviews = event["interviews"]
        action_type = event["action_type"]
        self.send(text_data=json.dumps({"data": interviews, "action_type": action_type}))


    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        action_demanded = data["action"]
        if action_demanded == "get_interviews":
            self.send_interviews()
        elif action_demanded == "update_interview":
            self.update_interview(data["data"])
        elif action_demanded == "fetch_interview":
            self.fetch_interview(data["data"])

    def connect(self):
        self.round_id = self.scope["url_route"]["kwargs"]["round_id"]
        self.round_group_name = f"round_{self.round_id}"
        
        async_to_sync(self.channel_layer.group_add)(
            self.round_group_name,
            self.channel_name
        )
        return super().connect()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.round_group_name,
            self.channel_name
        )