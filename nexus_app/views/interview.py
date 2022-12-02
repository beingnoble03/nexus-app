from rest_framework import viewsets
from nexus_app.api.serializers.message import MessageSerializer
from nexus_app.models import Round, Applicant
from nexus_app.api.serializers.interview import InterviewSerializer
from nexus_app.models import Interview, Message
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import InterviewDateAndTimeFilterSet
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework.decorators import action
from nexus_app.permissions import Is3or4y
import pandas


class InterviewViewSet(viewsets.ModelViewSet):
    """
    A Model ViewSet for Interviews. Search Fields include Applicant Name, 
    Panel Place, Applicant Enrolment Number. Filtering queryset can be done
    passing 'completed' as a parameter and Ordering can be done based on any
    field. For example,
    '/api/interviews/?search=Noble&ordering=time_assigned&completed=true'
    is a sample url.
    """
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    serializer_class = InterviewSerializer
    # queryset = Interview.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,
                       DjangoFilterBackend, ]
    filterset_class = InterviewDateAndTimeFilterSet
    search_fields = ['applicant__name', 'panel__place',
                     'applicant__enrolment_number', ]
    ordering_fields = '__all__'

    def get_queryset(self):
        min_marks_params = self.request.query_params.get("min_marks")
        max_marks_params = self.request.query_params.get("max_marks")
        top_percentage_params = self.request.query_params.get("top_percentage")

        queryset = Interview.objects.annotate(total_marks = Coalesce(Sum("section_marks_set__obtained_marks"), 0))        
        if self.request.user.is_master:
            if min_marks_params and not max_marks_params:
                queryset = Interview.objects.annotate(total_marks = Coalesce(Sum("section_marks_set__obtained_marks"), 0)).filter(total_marks__gte=int(min_marks_params))
                print(queryset.all().count())
            if max_marks_params and not min_marks_params:
                queryset = Interview.objects.annotate(total_marks = Coalesce(Sum("section_marks_set__obtained_marks"), 0)).filter(total_marks__lte=int(max_marks_params))
            if max_marks_params and min_marks_params:
                queryset = Interview.objects.annotate(total_marks = Coalesce(Sum("section_marks_set__obtained_marks"), 0)).filter(total_marks__lte=int(max_marks_params), total_marks__gte=int(min_marks_params))
            if top_percentage_params == "true":
                queryset = queryset.order_by("-total_marks")
        number_of_interviews = queryset.count()
        return queryset


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "is3yor4y": self.request.user.is_master
        })
        return context

    def create(self, request, *args, **kwargs):
        """
        Requires a list of applicant_ids with round_id
        """
        request_data = request.data
        for applicant_id in request_data.get("applicant_ids"):
            round_id = request_data.get("round_id")
            serialized_data = {
                "applicant": applicant_id,
                "round": round_id,
                "completed": request_data.get("completed"),
            }
            applicant = Applicant.objects.get(id = applicant_id)
            already_exists = Interview.objects.filter(applicant = applicant, round__id = round_id).count() != 0
            if not already_exists:
                serializer = InterviewSerializer(data=serialized_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        return Response("Created the instances.", status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @action(
        methods=["POST", ],
        detail=False,
        url_path="csvFile",
        url_name="csvFile",
        permission_classes = [IsAuthenticated, ],
        authentication_classes= [TokenAuthentication, ]
    )
    def add_applicants_to_test_round(self, request):
        print(request.FILES)
        file = pandas.read_csv(request.FILES.get("csvFile"))
        print(file.iterrows())
        round_id = request.POST.get("round_id")
        round_required = Round.objects.get(id = round_id)
        for index, row in file.iterrows():
            applicant_already_exists = Applicant.objects.filter(enrolment_number = row["Enrolment Number"]).count() != 0
            if applicant_already_exists:
                applicant = Applicant.objects.get(enrolment_number = row["Enrolment Number"])
                applicant.round.add(round_required)
                interview_already_exists = Interview.objects.filter(applicant = applicant, round=round_required).count() != 0
                if not interview_already_exists:
                    interview = Interview.objects.create(
                        applicant = applicant,
                        round = round_required,
                        completed = False
                    )
            else:
                applicant = Applicant.objects.create(
                    name=row["Name"],
                    enrolment_number=row["Enrolment Number"],
                    mobile=row["Mobile"],
                    branch=row["Branch"],
                    role=row["Role"],
                    email=row["Email"],
                    year=row["Year"]
                )
                interview = Interview.objects.create(
                    applicant = applicant,
                    round = round_required,
                    completed = False
                )
                
        return Response({
            "message": "Created and updated all interviews successfully."
        }, status=status.HTTP_201_CREATED)


    @action(
        methods=["GET", ],
        detail=True,
        url_path="messages",
        url_name="messages",
        permission_classes = [IsAuthenticated, Is3or4y, ],
        authentication_classes= [TokenAuthentication, ]
    )
    def get_messages(self, request, **kwargs):
        messages = Message.objects.filter(interview__id=kwargs["pk"])
        serializer = MessageSerializer(instance=messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)