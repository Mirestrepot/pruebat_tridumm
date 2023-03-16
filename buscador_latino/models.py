from django.db import models

# Create your models here.


class Search(models.Model):
    search_query = models.CharField(max_length=200)
    search_result_title = models.CharField(max_length=255)
    search_result_summary = models.TextField()
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search_query
    
class InfoData(models.Model):
    num_searches = models.IntegerField()
    first_search = models.CharField(max_length=200)
    last_search = models.CharField(max_length=200)
    search_text = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)
    last_num_searches = models.IntegerField()
    def __str__(self):
        return self.search_text