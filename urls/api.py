from rest_framework import routers

from modules.example.views.FakeModelViewSet import FakeModelViewSet

router = routers.DefaultRouter()
router.register(r'fakemodel', FakeModelViewSet)