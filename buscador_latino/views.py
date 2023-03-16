from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import SearchSerializer
from .models import Search
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import date, datetime, timedelta, timezone
from django.views.generic import TemplateView
import wikipediaapi

from pymongo import MongoClient

client = MongoClient('mongodb+srv://mirestrepot:Y34589ok.@twitterapi.tixzlnu.mongodb.net/?retryWrites=true&w=majority')
db = client['prueba-tecnica']
db_collection = db['buscador_latino_search']


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SearchSerializer
    template_name = 'index.html'
    context_object_name = 'search_view'


class WikipediaSearchView(APIView):
    """Search in wikipedia

    Args:
        search_query: str 
    return:  
        page-->str
        title-->str
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        search_query = request.GET.get('search')
        wiki = wikipediaapi.Wikipedia('en')
        page = wiki.page(search_query)
        title = page.title
        summary = page.summary
        if page.exists():
            search_result = Search(
                search_query=search_query,
                search_result_title=page.title,
                search_result_summary=page.summary,
                published_at=datetime.now()
            )
            search_result.save()
            context = {
                'search_query': search_query,
                'title': page.title,
                'summary': page.summary,
            }

            return Response(context)

class SearchResultsView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_text = self.request.GET.get('info_search')
        if search_text:
            searches = Search.objects.filter(search_query=search_text)
            num_searches = searches.count()
            if num_searches > 0:
                first_search = searches.first()
                last_search = searches.last()
                context['num_searches'] = num_searches
                context['first_search'] = first_search
                context['last_search'] = last_search
                context['search_text'] = search_text
        return context


