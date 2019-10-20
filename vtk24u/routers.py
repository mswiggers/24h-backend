from rest_framework import routers
from competition.viewsets import LapViewSet, RunnerViewSet, GroupViewSet, UniversityViewSet, HappyHourViewSet, GroupScoreViewSet

router = routers.SimpleRouter()
router.register(r'lap', LapViewSet)
router.register(r'group', GroupViewSet)
router.register(r'university', UniversityViewSet)
router.register(r'happyhour', HappyHourViewSet)
router.register(r'score', GroupScoreViewSet)
router.register(r'runner', RunnerViewSet, base_name='runner-case-insensitive')
urlpatterns = router.urls