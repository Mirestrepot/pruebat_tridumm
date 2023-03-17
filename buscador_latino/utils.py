

from datetime import datetime
from buscador_latino.models import InfoData, Search


def last_num_search(search_query):
    try:
        info_searches = InfoData.objects.filter(search_text=search_query)
        cont = info_searches.count()
        
        if cont > 1  :
            last_num_searches = info_searches.order_by('-created_at').first()
            return int(last_num_searches.num_searches)
        else:
            last_num_searches = 1
            return last_num_searches
    except:
        last_num_searches = 0
        return last_num_searches

            

def save_info_data(search_query):
    searches = Search.objects.filter(search_query=search_query) 
    try:
        if search_query:
    # Retrieve search results for the given search query

            num_searches = searches.count()
            first_search = searches.order_by('published_at').first()
            last_search = searches.order_by('-published_at').first()
            if num_searches < 1:
                num_searches=0
            first_search=first_search.published_at
            last_search=last_search.published_at 
            last_num_searches=last_num_search(search_query)

            info_schema = InfoData(
                num_searches=num_searches,
                first_search=first_search,
                last_search=last_search,
                search_text=search_query,
                created_at=datetime.now(),
                last_num_searches=last_num_searches
                )
        return info_schema
    except:
        return None


