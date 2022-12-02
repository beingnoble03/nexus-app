from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from nexus_app.permissions import Is3or4y
from nexus_app.models import Applicant


class RemarksView(APIView):
    permission_classes = [IsAuthenticated, Is3or4y, ]
    authentication_classes = [TokenAuthentication, ]

    def get(self, request):
        applicant_id = request.GET.get('applicant_id')
        applicant = Applicant.objects.get(id=applicant_id)
        rounds = applicant.round.all()
        questions = []
        for round in rounds:
            if round.round_type == "T":
                for test in round.tests.all():
                    for section in test.section_set.all():
                        for question in section.question_set.all():
                            question_dict = {}
                            for question_score in question.question_scores.filter(applicant__id = applicant_id):
                                if question_score.remarks:
                                    question_dict["id"] = question.id
                                    question_dict["title"] = question.title
                                    question_dict["remarks"] = question_score.remarks
                                    question_dict["obtained_marks"] = question_score.obtained_marks
                                    question_dict["maximum_marks"] = question.maximum_marks
                                    question_dict["test_title"] = test.title
                                    question_dict["round_name"] = round.round_name
                                    questions.append(question_dict)
        interviews = applicant.interview_set.all()
        interview_list = []
        for interview in interviews:
            interview_dict = {
                "id": interview.id,
                "title": interview.round.round_name,
                "remarks": interview.remarks,
            }
            interview_list.append(interview_dict)
        return Response({
            "questions": questions,
            "interviews": interview_list,
        })