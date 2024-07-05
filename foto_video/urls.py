from rest_framework import routers

from foto_video.views import VideoViewSet, FotoViewSet

router = routers.SimpleRouter()
router.register(r'video', VideoViewSet)
router.register(r'foto', FotoViewSet)
urlpatterns = router.urls
