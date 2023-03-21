from django.urls import path
from rest_framework import routers

from buscador_latino.views_set import InfoViewSet
from .views import ListInform, SearchViewSet, WikipediaSearchView, SearchResultsView

router = routers.DefaultRouter()
router.register(r'searches', SearchViewSet)
router.register(r'inform', InfoViewSet)

urlpatterns = [
    path('home/', WikipediaSearchView.as_view(), name='wikipedia_search'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('homepage/',ListInform.as_view())
]

urlpatterns += router.urls