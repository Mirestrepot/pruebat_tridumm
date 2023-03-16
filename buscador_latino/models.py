from django.db import models

# Create your models here.


class Search(models.Model):
    search_query = models.CharField(max_length=200)
    search_result_title = models.CharField(max_length=255)
    search_result_summary = models.TextField()

    def __str__(self):
        return self.search_query
