from django.db import models



# def user_directory_path(instance, filename):
#     return 'home/{0}/{1}'.format(instance.title, filename)

# class Post(models.Model):
#     class PostObjects(models.Manager):
#         def get_queryset(self):
#             return super().get_queryset()
    
#     title = models.CharField(max_length=250)
#     image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
#     excerpt = models.TextField(null=True)
#     content = models.TextField()
#     slug = models.SlugField(max_length=250, unique_for_date='published', null=False, unique=True)
#     published = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
#     objects = models.Manager()
#     postobjects = PostObjects()

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