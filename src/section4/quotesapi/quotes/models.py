from django.db import models


class Quote(models.Model):
    quote_author = models.CharField(max_length=120)
    quote_body = models.TextField()
    context = models.TextField()
    source = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quote_author} {self.source}'
