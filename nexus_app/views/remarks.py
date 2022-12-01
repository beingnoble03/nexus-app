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
        print(applicant)
        rounds = applicant.round.all()
        test_rounds = []
        for round in rounds:
            if round.round_type == "T":
                round_dict = {
                    "id": round.id,
                    "title": round.round_name,
                }
                tests = []
                for test in round.tests.all():
                    test_dict = {
                        "id": test.id,
                        "title": test.title,
                    }
                    sections = []
                    for section in test.section_set.all():
                        section_dict = {
                            "id": section.id,
                            "title": section.title,
                        }
                        questions = []
                        for question in section.question_set.all():
                            question_dict = {}
                            for question_score in question.question_scores.all():
                                if question_score.remarks:
                                    question_dict["id"] = question.id
                                    question_dict["title"] = question.title
                                    question_dict["remarks"] = question_score.remarks
                                    question_dict["obtained_marks"] = question_score.obtained_marks
                                    question_dict["maximum_marks"] = question.maximum_marks
                                    questions.append(question_dict)
                                    print("he")
                        if len(questions):
                            section_dict["questions"] = questions
                            sections.append(section_dict)
                    if len(sections):
                        test_dict["sections"] = sections
                        tests.append(test_dict)
                round_dict["tests"] = tests
                if len(tests):
                    test_rounds.append(round_dict)
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
            "test_rounds": test_rounds,
            "interviews": interview_list,
        })