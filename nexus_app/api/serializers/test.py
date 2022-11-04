from rest_framework import serializers
from nexus_app.models import Test, Score
from .section import SectionWithQuestionSerializer


class TestApplicantSerializer(serializers.ModelSerializer):
    applicants = serializers.SerializerMethodField("get_test_applicants")

    def get_test_applicants(self, instance):
        number_of_questions = 0
        section_list = instance.section_set.all()
        for section in section_list:
            number_of_questions += section.question_set.count()
        applicant_list = []
        search_params = self.context["request"].query_params.get(
            "search", None
        )
        evaluated_params = self.context["request"].query_params.get(
            "evaluated", None
        )
        min_marks_params = self.context["request"].query_params.get(
            "min_marks", None
        )
        max_marks_params = self.context["request"].query_params.get(
            "max_marks", None
        )
        top_percentage_params = self.context["request"].query_params.get(
            "top_percentage", None
        )

        for test_applicant in instance.round.applicants.all():
            if not search_params or test_applicant.name.lower().find(search_params.lower()) != -1 or str(test_applicant.enrolment_number).find(search_params) != -1:
                applicant_dict = {}
                applicant_dict["id"] = test_applicant.id
                applicant_dict["name"] = test_applicant.name
                applicant_dict["enrolment_number"] = test_applicant.enrolment_number
                applicant_dict["mobile"] = test_applicant.mobile
                total_marks = 0
                for score in Score.objects.filter(
                    applicant=test_applicant,
                    question__section__test=instance
                ):
                    total_marks += score.obtained_marks
                if number_of_questions != Score.objects.filter(
                        applicant=test_applicant,
                        question__section__test=instance).count():
                    applicant_dict["status"] = "Not Evaluated"
                else:
                    applicant_dict["status"] = "Evaluated"
                if self.context.get("is3yor4y"):
                    applicant_dict["total_marks"] = total_marks
                if (not evaluated_params or (evaluated_params == "true" and applicant_dict["status"] == "Evaluated") or (evaluated_params == "false" and applicant_dict["status"] == "Not Evaluated")):
                    if (not min_marks_params or not self.context.get("is3yor4y") or (int(min_marks_params) <= total_marks)):
                        if (not max_marks_params or not self.context.get("is3yor4y") or (int(max_marks_params) >= total_marks)):
                            applicant_list.append(applicant_dict)

        if self.context.get("is3yor4y") and (top_percentage_params == "true"):
            new_list = sorted(
                applicant_list, key=lambda d: d["total_marks"], reverse=True)
            return new_list
        return applicant_list

    class Meta:
        model = Test
        fields = ['id', 'title', 'applicants', 'round']


class TestSectionSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField("get_sections_with_questions")

    def get_sections_with_questions(self, instance):
        section_queryset = instance.section_set
        return SectionWithQuestionSerializer(section_queryset, many=True).data

    class Meta:
        model = Test
        fields = ['id', 'title', 'sections']
