from django.urls import path
from rest_framework import routers
from .views import  SearchViewSet,WikipediaSearchView

router = routers.DefaultRouter()

router.register(prefix='search', basename="search", viewset=SearchViewSet)


urlpatterns = [
    path('wikipedia/search/', WikipediaSearchView.as_view(), name='wikipedia_search'),
]
urlpatterns += router.urls