from rest_framework import serializers
from nexus_app.models import Test, Score
from .section import SectionWithQuestionSerializer

class TestApplicantSerializer(serializers.ModelSerializer):
    applicants = serializers.SerializerMethodField("get_test_applicants")
    
    def get_test_applicants(self, instance):
        number_of_questions = 0
        section_list = instance.section_set.all()
        for section in section_list:
            number_of_questions =+ section.question_set.count()
        applicant_list = []
        applicant_dict = {}

        for test_applicant in instance.round.applicants.all():
            applicant_dict["id"] = test_applicant.id
            applicant_dict["name"] = test_applicant.name
            applicant_dict["enrolment_number"] = test_applicant.enrolment_number
            applicant_dict["mobile"] = test_applicant.mobile
            if number_of_questions != Score.objects.filter(
                applicant=test_applicant, 
                question__section__test = instance).count():
                applicant_dict["status"] = "Not Evaluated"
            else:
                applicant_dict["status"] = "Evaluated"
            applicant_list.append(applicant_dict)
        return applicant_list

    class Meta:
        model = Test
        fields = ['id', 'title', 'applicants']

class TestSectionSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField("get_sections_with_questions")

    def get_sections_with_questions(self, instance):
        section_queryset = instance.section_set
        return SectionWithQuestionSerializer(section_queryset, many=True).data

    class Meta:
        model = Test
        fields = ['id', 'title', 'sections']