from rest_framework.routers import DefaultRouter
from nexus_app.views import RoundNameViewSet, RoundViewset
from nexus_app.views.season import SeasonViewSet


router = DefaultRouter()
router.register(r"seasons", SeasonViewSet, "season-viewset")
router.register(r"roundNames", RoundNameViewSet, "round-names")
router.register(r"roundDetails", RoundViewset, "round-details")
urlpatterns = router.urls