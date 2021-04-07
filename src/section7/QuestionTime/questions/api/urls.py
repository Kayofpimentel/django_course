from django.urls import include, path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from questions.api import views as vw

router = DefaultRouter()
router.register(r'questions', vw.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
