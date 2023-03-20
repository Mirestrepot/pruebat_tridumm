from django.contrib import admin
from buscador_latino.models import Search
# Register your models here.

# admin.site.register(Post)


@admin.register(Search)
class PostAdmin(admin.ModelAdmin):
    fields = ["search_query"]
    list_display = ("search_query","search_result_title","search_result_summary","published_at")
    list_filter = ["search_query","search_result_title","search_result_summary","published_at"]
    search_fields = ["search_query","published_at"]