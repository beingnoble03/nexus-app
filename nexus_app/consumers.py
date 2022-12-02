from channels.generic.websocket import WebsocketConsumer
from nexus_app.models import Panel, Interview, ImgMember, Message
from nexus_app.api.serializers.interview import InterviewSerializer
from nexus_app.api.serializers.message import MessageSerializer
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


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        self.interview_id = self.scope["url_route"]["kwargs"]["interview_id"]
        self.interview_group_name = f"interview_{self.interview_id}"
        
        async_to_sync(self.channel_layer.group_add)(
            self.interview_group_name,
            self.channel_name
        )
        return super().connect()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.interview_group_name,
            self.channel_name
        )

    def create_message(self, data):
        print(data)
        interview = Interview.objects.get(id=data["interview"])
        img_member = ImgMember.objects.get(id=data["user_id"])
        message = data["message"]
        new_message = Message.objects.create(interview = interview, author = img_member, message = message)
        new_message.save()
        serializer = MessageSerializer(instance=new_message)
        async_to_sync(self.channel_layer.group_send)(
            self.interview_group_name, {"type": "message", "message": serializer.data, "action_type": "new_message"}
        )

    def message(self, event):
        message = event["message"]
        action_type = event["action_type"]
        self.send(text_data=json.dumps({"data": message, "action_type": action_type}))

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        action_demanded = data["action"]
        if action_demanded == "create_message":
            self.create_message(data["data"])