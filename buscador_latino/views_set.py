from django.shortcuts import render
from rest_framework import viewsets, permissions

from buscador_latino.utils import last_num_search, save_info_data
from .serializers import InformSerializer, SearchSerializer
from .models import InfoData, Search




class SearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows searches to be viewed or edited.
    """
    queryset = Search.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SearchSerializer
    template_name = 'index.html'
    context_object_name = 'search_view'

class InfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows searches to be Info Search.
    """
    queryset = InfoData.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = InformSerializer
    template_name = 'index.html'
    context_object_name = 'info_view'

