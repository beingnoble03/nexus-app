from rest_framework.routers import DefaultRouter
from nexus_app.views import RoundNameViewSet, RoundViewset
from nexus_app.views.round.applicant import ApplicantViewSet
from nexus_app.views.round.interview import InterviewViewSet
from nexus_app.views.round.interview_marks import InterviewMarksView
from nexus_app.views.round.round_interview_sections import RoundInterviewSectionViewSet
from nexus_app.views.round.interview_section import InterviewSectionViewSet
from nexus_app.views.round.panel import PanelViewSet
from nexus_app.views.round.question import QuestionViewset
from nexus_app.views.round.round_interview_list import RoundInterviewViewSet
from nexus_app.views.round.section_marks import SectionMarksViewSet
from nexus_app.views.round.test_list import TestApplicantViewSet
from nexus_app.views.round.test_score import TestScoreView
from nexus_app.views.round.members import MemberViewSet
from nexus_app.views.round.test_sections import TestSectionViewset
from nexus_app.views.season import SeasonViewSet
from django.urls import path

router = DefaultRouter()
router.register(r"seasons", SeasonViewSet, "season-viewset")
router.register(r"roundNames", RoundNameViewSet, "round-names")
router.register(r"roundDetails", RoundViewset, "round-details")
router.register(r"testApplicants", TestApplicantViewSet, "test-applicant-list")
router.register(r"testSections", TestSectionViewset, "test-sections-viewset")
router.register(r"questions", QuestionViewset, "question-viewset")
router.register(r"roundInterviewSections", RoundInterviewSectionViewSet, "round-interview-sections-viewset")
router.register(r"interviewSections", InterviewSectionViewSet, "interview-sections-viewset")
router.register(r"members", MemberViewSet, "members-viewset")
router.register(r"panels", PanelViewSet, "panels-viewset")
router.register(r"roundInterviews", RoundInterviewViewSet, "round-interview-viewset")
router.register(r"applicants", ApplicantViewSet, "applicant-viewset")
router.register(r"interviews", InterviewViewSet, "interview-viewset")
router.register(r"seasons", SeasonViewSet, "season-viewset")
router.register(r"sectionMarks", SectionMarksViewSet, "section-marks-viewset")
urlpatterns = router.urls

urlpatterns += [
    path(r"testScore/", TestScoreView.as_view()),
    path(r"interviewMarks/", InterviewMarksView.as_view()),
]