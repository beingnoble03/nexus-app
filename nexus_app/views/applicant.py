from rest_framework import viewsets
from nexus_app.models import Round
from nexus_app.api.serializers.applicant import ApplicantSerializer
from nexus_app.models import Applicant
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
import pandas
from rest_framework.response import Response
from rest_framework import status


class ApplicantViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    search_fields = ['name', 'enrolment_number', ]
    ordering_fields = ['name', ]
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all()

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
            already_exists = Applicant.objects.filter(enrolment_number = row["Enrolment Number"]).count() != 0
            if already_exists:
                applicant = Applicant.objects.get(enrolment_number = row["Enrolment Number"])
                applicant.round.add(round_required)
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
                applicant.round.add(round_required)
        return Response({
            "message": "Created and updated all applicants successfully"
        }, status=status.HTTP_201_CREATED)