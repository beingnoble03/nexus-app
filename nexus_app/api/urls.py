from rest_framework.routers import DefaultRouter
from nexus_app.views.current_user import CurrentUserViewSet
from nexus_app.views import *
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
router.register(r"current_user", CurrentUserViewSet, "current-user-viewset")
router.register(r"sections", SectionViewSet, "current-user-viewset")
urlpatterns = router.urls

urlpatterns += [
    path(r"testScore/", TestScoreView.as_view()),
    path(r"interviewMarks/", InterviewMarksView.as_view()),
]