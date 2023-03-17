from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions

from buscador_latino.utils import last_num_search, save_info_data
from .serializers import SearchSerializer
from .models import InfoData, Search
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import date, datetime, timedelta, timezone
from django.views.generic import TemplateView
import wikipediaapi


# Connect to MongoDB Atlas cluster

class SearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows searches to be viewed or edited.
    """
    queryset = Search.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SearchSerializer
    template_name = 'index.html'
    context_object_name = 'search_view'


class WikipediaSearchView(APIView):
    """
    API endpoint that searches for a query in Wikipedia.

    Args:
        search_query (str): The search query to look up on Wikipedia.

    Returns:
        page (str): The Wikipedia page matching the search query.
        title (str): The title of the Wikipedia page matching the search query.
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
            # Save search query result to MongoDB Atlas
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
    """
    API endpoint that retrieves search results for a given search query.

    Args:
        search_text (str): The search query to retrieve search results for.

    Returns:
        num_searches (int): The number of searches for the given search query.
        first_search (Search): The first search result for the given search query.
        last_search (Search): The most recent search result for the given search query.
        search_text (str): The search query to retrieve search results for.
        last_num_searches (int): The number of search results for the most recent search.
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_text = self.request.GET.get('search_text')
        if search_text:
            # Retrieve search results for the given search query
            searches = Search.objects.filter(search_query=search_text)
            #info_searches = InfoData.objects.filter(search_text=search_text)
            last_num_search(search_text)

            last_num_searches = last_num_search(search_text)
            
                
            num_searches = searches.count()
            first_search = searches.order_by('published_at').first()
            last_search = searches.order_by('-published_at').first()
            if num_searches < 1:
                num_searches=1
            context['num_searches'] = num_searches
            context['first_search'] = first_search
            context['last_search'] = last_search
            context['search_text'] = search_text
            context['last_num_searches'] = last_num_searches

            first_search=first_search.published_at
            last_search=last_search.published_at 
    
            
            new_data=save_info_data(search_text)
            if new_data != None:
                new_data.save()

            return context

