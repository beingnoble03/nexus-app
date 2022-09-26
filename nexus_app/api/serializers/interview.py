from nexus_app.models import Interview
from rest_framework import serializers
from .section_marks import SectionMarksSerializer
from .panel import PanelSerializer

class InterviewSerializer(serializers.ModelSerializer):
    applicant_details = serializers.SerializerMethodField("get_applicant_details")

    def get_applicant_details(self, instance):
        details = {
            "id": instance.applicant.id,
            "name": instance.applicant.name,
            "enrollment_number": instance.applicant.enrollment_number,
            "mobile": instance.applicant.mobile
        }
        return details

    class Meta:
        model = Interview
        fields = '__all__'

class InterviewSectionMarksSerializer(serializers.ModelSerializer):
    section_marks = serializers.SerializerMethodField('get_section_details')
    applicant_details = serializers.SerializerMethodField('get_applicant_details')

    def get_section_details(self, instance):
        return SectionMarksSerializer(instance.section_marks_set, many = True).data

    def get_applicant_details(self, instance):
        details = {
            "id": instance.applicant.id,
            "name": instance.applicant.name,
            "enrollment_number": instance.applicant.enrollment_number,
        }
        return details

    class Meta:
        model = Interview
        fields = ['id', 'applicant_details', 'section_marks', 'remarks']