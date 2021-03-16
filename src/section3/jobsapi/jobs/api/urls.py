from django.urls import path
from .views import (
    CompanyViewCreateApiView, JobDetailApiView, JobListCreateApiView)

urlpatterns = [
    path("jobs/", JobListCreateApiView.as_view(),
         name="job-list"),

    path("job/<int:pk>", JobDetailApiView.as_view(),
         name="available-job"),

    path("companies/", CompanyViewCreateApiView.as_view(),
         name="company-list"), ]
