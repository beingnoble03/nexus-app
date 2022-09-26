from rest_framework import serializers
from .interview_section import InterviewSectionSerializer
from .interview import InterviewSerializer
from nexus_app.models import Round

class RoundNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ['round_name']

class RoundSerializer(serializers.ModelSerializer):
    test_titles = serializers.SerializerMethodField('test_title_list')

    def test_title_list(self, instance):
        title_list = []
        test_dict = {}
        for test in instance.tests.all():
            test_dict["id"] = test.id
            test_dict["title"] = test.title
            title_list.append(test_dict)
        return title_list

    class Meta:
        model = Round
        fields = '__all__'

class RoundInterviewSectionSerializer(serializers.ModelSerializer):
    interview_section_details = serializers.SerializerMethodField("get_interview_section_details")

    def get_interview_section_details(self, instance):
        return InterviewSectionSerializer(instance.interview_sections, many = True).data

    class Meta:
        model = Round
        fields = ['id', 'round_name', 'interview_section_details']

class RoundInterviewListSerializer(serializers.ModelSerializer):
    interviews = serializers.SerializerMethodField("get_interviews")

    def get_interviews(self, instance):
        return InterviewSerializer(instance.interviews.all(), many = True).data

    class Meta:
        model = Round
        fields = ['round_name', 'id', 'interviews']