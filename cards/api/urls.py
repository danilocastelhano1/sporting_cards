from django.urls import include, path
from rest_framework import routers

from .views import TagViewset
from .views import CardViewset


router = routers.DefaultRouter()
router.register(r"tag", TagViewset)
router.register(r"card", CardViewset)


urlpatterns = [
    path(r"api/", include(router.urls)),
]
