from django.urls import path
from .views import EbookListCreateAPIView, EbookDetailApiView, ReviewCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    path('ebooks/', EbookListCreateAPIView.as_view(), name='ebook-list'),
    path('ebook/<int:pk>/', EbookDetailApiView.as_view(), name='ebook-detail'),
    path('ebook/<int:ebook_pk>/review/',
         ReviewCreateAPIView.as_view(), name='ebook-review'),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail')
]