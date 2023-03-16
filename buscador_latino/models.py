from django.db import models

# Create your models here.


class Search(models.Model):
    search_query = models.CharField(max_length=200)
    search_result_title = models.CharField(max_length=255)
    search_result_summary = models.TextField()
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search_query

class InfoSearch(models.Model):
    search_query = models.CharField(max_length=200)
    num_searches = models.ImageField()
    first_search = models.DateTimeField()
    last_search = models.DateTimeField
    last_week_searches = models.DateTimeField