from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=120)
    company_email = models.CharField(max_length=200)
    hiring = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company_name}'


class JobOffer(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='jobs')
    job_title = models.CharField(max_length=200)
    job_descriptions = models.TextField(blank=True)
    salary = models.FloatField()
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.job_title} {self.company}'
