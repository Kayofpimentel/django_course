from django.urls import include, path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from questions.api import views as vw

router = DefaultRouter()
router.register(r'questions', vw.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/answer/',
         vw.AnswerCreateAPIView.as_view(),
         name='answer_create'),
    path('questions/<slug:slug>/answers/',
         vw.AnswerListAPIView.as_view(),
         name='answer_list'),
    path('answers/<int:pk>/',
         vw.AnswerRUDAPIView.as_view(), name='answer_detail'),
    path('answers/<int:pk>/like/',
         vw.AnswerLikeAPIView.as_view(), name='answer_like')
]
