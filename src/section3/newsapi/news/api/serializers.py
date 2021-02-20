from rest_framework import serializers as srs
from news.models import Article


class ArticleSerializer(srs.Serializer):
    id = srs.IntegerField(read_only=True)
    author = srs.CharField()
    title = srs.CharField()
    description = srs.CharField()
    body = srs.CharField()
    location = srs.CharField()
    publication_date = srs.DateField()
    published = srs.BooleanField()
    created_at = srs.DateTimeField(read_only=True)
    updated_at = srs.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(f'{validated_data:}')
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get(
            'publication_date', instance.publication_date)
        instance.published = validated_data.get(
            'published', instance.published)
