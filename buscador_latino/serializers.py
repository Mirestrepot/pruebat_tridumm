from rest_framework import serializers

#Models
from .models import Search,InfoData
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ("id", "search_query","search_result_title","search_result_summary","published_at")
        read_only_fields = ("published_at",)
        
class InformSerializer(serializers.ModelSerializer):
     class Meta:
        model = InfoData
        fields = ("num_searches", "first_search","last_search","search_text","created_at","last_num_searches")
        read_only_fields = ("created_at",)