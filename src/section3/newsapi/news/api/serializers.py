from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers as srs
from news.models import Article


class ArticleSerializer(srs.ModelSerializer):

    time_since_publication = srs.SerializerMethodField()

    class Meta:
        model = Article
        # fields = "__all__"  # Define that we want all the fields of our model
        # fields = ("title","description","body") Example to define some fields
        exclude = "id", "created_at", "updated_at"

    def get_time_since_publication(_, object):
        publication_data = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_data, now)
        return time_delta

    def validate(self, data):
        """ Check that description and title are different """
        if data["title"] == data["description"]:
            raise srs.ValidationError(
                "Title and Description must be different ")
        return data

    def validate_title(self, value):
        if len(value) < 30:
            raise srs.ValidationError("The title is too short")
        return value

# class ArticleSerializer(srs.Serializer):
#     id = srs.IntegerField(read_only=True)
#     author = srs.CharField()
#     title = srs.CharField()
#     description = srs.CharField()
#     body = srs.CharField()
#     location = srs.CharField()
#     publication_date = srs.DateField()
#     published = srs.BooleanField()
#     created_at = srs.DateTimeField(read_only=True)
#     updated_at = srs.DateTimeField(read_only=True)

#     def create(_, validated_data):
#         print(f'{validated_data:}')
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get(
#             'description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get(
#             'publication_date', instance.publication_date)
#         instance.published = validated_data.get(
#             'published', instance.published)
#         instance.save()
#         print(f'{validated_data:}')
#         return instance

#     def validate(self, data):
#         """ Check that description and title are different """
#         if data["title"] == data["description"]:
#             raise srs.ValidationError(
#                 "Title and Description must be different ")
#         return data

#     def validate_title(self, value):
#         if len(value) < 60:
#             raise srs.ValidationError("The title is too short")
#         return value
