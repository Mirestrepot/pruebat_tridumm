from rest_framework import serializers

#Models
from .models import Search
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ("id", "search_query","search_result_title","search_result_summary","published_at")
        read_only_fields = ("published_at",)
        
class InformSerializer(serializers.ModelSerializer):
     class Meta:
        model = Search
        fields = ("id", "search_query","search_result_title","search_result_summary","published_at")
        read_only_fields = ("published_at",)