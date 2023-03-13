from django.urls import include, path
from rest_framework import routers

from .views import TagViewset

router = routers.DefaultRouter()
router.register(r"tag", TagViewset)

urlpatterns = [
    path(r"api/", include(router.urls)),
]
