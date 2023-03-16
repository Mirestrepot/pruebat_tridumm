from django.urls import path
from rest_framework import routers
from .views import SearchViewSet, WikipediaSearchView, SearchResultsView

router = routers.DefaultRouter()
router.register(r'searches', SearchViewSet)

urlpatterns = [
    path('', WikipediaSearchView.as_view(), name='wikipedia_search'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]

urlpatterns += router.urls