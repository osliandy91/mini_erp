from django.urls import path, include
from rest_framework import routers
from projects import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectView, 'projects')

#api versioning
urlpatters = [
    path("api/v1", include(router.url))
]