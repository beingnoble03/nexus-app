from rest_framework import serializers
from ...models import Message

class MessageSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField("get_author_name")
    author_image = serializers.SerializerMethodField("get_author_image")

    def get_author_name(self, instance):
        return instance.author.name

    def get_author_image(self, instance):
        return instance.author.image

    class Meta:
        model = Message
        fields = '__all__'