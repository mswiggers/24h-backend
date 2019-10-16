from rest_framework import routers
from competition.viewsets import LapViewSet, RunnerViewSet, GroupViewSet, UniversityViewSet, HappyHourViewSet

router = routers.SimpleRouter()
router.register(r'lap', LapViewSet)
router.register(r'runner', RunnerViewSet)
router.register(r'group', GroupViewSet)
router.register(r'university', UniversityViewSet)
router.register(r'happyhour', HappyHourViewSet)
urlpatterns = router.urls