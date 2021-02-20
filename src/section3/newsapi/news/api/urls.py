from django.conf.urls import url
from django.urls import path
from news.api.views import (ArticleDetailApiView, ArticleListCreateApiView)
# from news.api.views import (article_list_create_api_view,
#                             article_detail_api_view)

urlpatterns = [
    path("articles/", ArticleListCreateApiView.as_view(),
         name="article_list"),

    path("article/<int:pk>", ArticleDetailApiView.as_view(),
         name="article_detail")]
# path("articles/", article_list_create_api_view, name="article_list"),
# path("article/<int:pk>", article_detail_api_view, name="article_detail")]
