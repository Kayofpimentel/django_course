from django.db import models


class Ebook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=120)
