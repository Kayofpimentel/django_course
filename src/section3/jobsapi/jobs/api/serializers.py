from rest_framework import serializers as srs
from ..models import Company, JobOffer


class CompanySerializer(srs.ModelSerializer):

    jobs = srs.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='available-job')

    class Meta:
        model = Company
        fields = '__all__'


class JobOfferSerializer(srs.ModelSerializer):

    class Meta:
        model = JobOffer
        exclude = ("id", "created_at",)
