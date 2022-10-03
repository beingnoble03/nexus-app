from rest_framework.views import APIView
from rest_framework.response import Response
from nexus_app.models import Question, Score, Applicant, Test, Section
from django.shortcuts import get_object_or_404, get_list_or_404
from nexus_app.api.serializers.img_member import ImgMemberSerializer
from nexus_app.api.serializers.score import ScoreSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from nexus_app.permissions import Is3or4y

class TestScoreView(APIView):
    """
    Get a list of scores and questions of a particular applicant in a 
    particular test, create or update score instances using 'post' request.
    """
    permission_classes = [IsAuthenticated, Is3or4y]
    authentication_classes = [TokenAuthentication, ]  
    def get(self, request):
        applicant_id = request.GET.get('applicant_id', None)
        test_id = request.GET.get('test_id', None)
        if applicant_id == None or test_id == None:
            return Response({
                "details": "applicant_id or test_id doesn't exist"
            })

        section_queryset = get_list_or_404(Section, test__id = test_id)
        sections = []
        for section in section_queryset:
            section_dict = {}
            section_dict["title"] = section.title
            try:
                question_queryset = Question.objects.filter(
                section__id = section.id)
            except:
                question_queryset = None
            questions = []
            for question in question_queryset:
                question_dict = {}
                try:
                    score = Score.objects.get(question = question,
                     applicant__id = applicant_id)
                except Score.DoesNotExist:
                    score = None
                # data = QuestionSerializer(question).data
                # data["scores"] = ScoreSerializer(score)
                question_dict["id"] = question.id
                question_dict["title"] = question.title
                question_dict["maximum_marks"] = question.maximum_marks
                question_dict["assignee"] = ImgMemberSerializer(
                    question.assignee, many = True).data
                if score:
                    question_dict["score_id"] = score.id
                    question_dict["obtained_marks"] = score.obtained_marks
                    question_dict["remarks"] = score.remarks
                else:
                    question_dict["score_id"] = None
                    question_dict["obtained_marks"] = None
                    question_dict["remarks"] = None
                questions.append(question_dict)
            section_dict["questions"] = questions
            sections.append(section_dict)
        
        applicant = get_object_or_404(Applicant, id = applicant_id)
        applicant_details = {
            "name": applicant.name,
            "enrolment_number": applicant.enrolment_number
        }

        test_details = {
            "title": Test.objects.get(id = test_id).title
        }
        return Response({
            "test_details": test_details,
            "applicant_details": applicant_details,
            "sections": sections,
        })

    def post(self, request):
        """
        To create/ edit Score instance, request_data should contain list
        of 'scores' which should include question, obtained_marks, applicant,
        remarks(optional).
        """
        request_data = request.data
        if request_data["scores"]:     
            for score in request_data["scores"]:
                if Score.objects.filter(applicant__id = score["applicant"],
                question__id = score["question"]).count():
                    self.update(request, score)
                else:
                    serialized_data = ScoreSerializer(data = score)
                    if serialized_data.is_valid():
                        serialized_data.save()

            return Response({
                "details": "Created Score Instances"
            }, status = status.HTTP_201_CREATED)
        else:
            return Response({
                "details": "Invalid format for post request."
            }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, score):
        """
        To update an existing score instance, pass the applicant,
        question, obtained_marks, remarks(optional).
        """
        score_instance = Score.objects.get(applicant__id = score["applicant"],
        question__id = score["question"])
        serialized_data = ScoreSerializer(instance = score_instance,
        data = score)
        if serialized_data.is_valid():
            serialized_data.save()
        else:
            return Response(serialized_data.errors,
            status = status.HTTP_400_BAD_REQUEST)

# from django.db.models import Q
# Q and F in django
# questions = Question.objects.filter(Q(section__test_id=test_id))
# scores = Score.objects.filter(question__in=questions, applicant_id=applicant_id)
# scores = Score.objects.filter(applicant_id=applicant_id, question__test_id=test_id)