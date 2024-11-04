from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=100, null=True, blank=True)
    born_location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    tags = ArrayField(models.CharField(max_length=30), blank=False, default=list)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)
    quote = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.quote


