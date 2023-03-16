from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import SearchSerializer
from .models import Search
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import datetime
from db.database import db_colection,client
# import wikipedia as wiki
import wikipediaapi

# Create your views here.



class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SearchSerializer
    template_name = 'index.html'
    context_object_name = 'search_view'
    
    

class WikipediaSearchView(APIView):
    """Search in wikipedia

    Args:
        search_text: str 
    return:  search_results-->str
    
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'
    
    def get(self, request):
        search_query = request.query_params.get('search')
        wiki = wikipediaapi.Wikipedia('en')
        page = wiki.page(search_query)
        title = page.title
        summary = page.summary


        #Crear una instancia del modelo WikipediaSearch y guardarla en la base de datos
        # Search.objects.create(search_query,
        #     search_result_title=title,
        #     search_result_summary=summary,
        #     published_at = datetime.now(),
        #)
        if page.exists():
            search_result = Search(
                search_query=search_query,
                search_result_title=title,
                search_result_summary=summary
                )
            db_colection.insert_one(search_result.__dict__)
            search_result.save()
            return Response({'title': page.title, 'summary': page.summary})
        else: raise HttpResponse.status_code(404)

        

