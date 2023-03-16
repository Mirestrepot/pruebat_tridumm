from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import SearchSerializer
from .models import Search
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import date,datetime, timedelta, timezone
from django.views.generic import TemplateView
#from db.database import db_colection
# import wikipedia as wiki
import wikipediaapi
import wikipedia

# Create your views here.
from pymongo import MongoClient

client = MongoClient('mongodb+srv://mirestrepot:Y34589ok.@twitterapi.tixzlnu.mongodb.net/?retryWrites=true&w=majority')
db = client['prueba-tecnica']
db_colection = db['buscador_latino_search']



class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SearchSerializer


    
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
                'search_text': search_query, 
                'title': page.title, 
                'summary': page.summary,
            }
        
            return Response(context)

        
    def get(self, request):
        search_query = request.GET.get('info_search')
        search_text = search_query
        search_results = Search.objects.filter(search_query=search_query)
        num_searches = search_results.count()
        first_search = search_results.order_by('published_at').first()
        last_search = search_results.order_by('-published_at').first()
        #last_week_searches = search_results.filter(published_now=datetime.now() - timedelta(days=7)).count()
        context = {
            'search_text': search_text,
            'num_searches': num_searches,
            'first_search': first_search,
            'last_search': last_search,
            }
        #'last_week_searches': last_week_searches,
        return Response(context)
    





# def get_info_search(search_query):
    

#     search_text = search_query
#     search_results = Search.objects.filter(search_query=search_query)
#     num_searches = search_results.count()
#     first_search = search_results.order_by('published_at').first()
#     last_search = search_results.order_by('-published_at').first()
#     #last_week_searches = search_results.filter(published_now=datetime.now() - timedelta(days=7)).count()
#     context = {
#         'search_text': search_text,
#         'num_searches': num_searches,
#         'first_search': first_search,
#         'last_search': last_search,
#         #'last_week_searches': last_week_searches,
#     }

