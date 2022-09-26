from rest_framework import serializers
from nexus_app.models import Section
from .question import QuestionWithAssigneeDetailsSerializer


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class SectionWithQuestionSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField("get_questions")

    def get_questions(self, instance):
        return QuestionWithAssigneeDetailsSerializer(instance.question_set, many=True).data

    class Meta:
        model = Section
        fields = '__all__'