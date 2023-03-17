# Prueba Tecnica Triduum
The project is a Django Rest Framework + HTML + MongoDB (Atlas) + CSS application that searches Wikipedia and displays a summary on the screen. It also generates a search report when a search is performed in the search bar.

## Installation
Clone the repository.
Install the dependencies by running pip install -r requirements.txt.
Configure the MongoDB connection in db/database.py by updating the client variable.
Run the server using the command python manage.py runserver.

## Endpoint
http://127.0.0.1:8000/ = API root the all gets 
http://127.0.0.1:8000/home = Index.html and all templetes
## Docker
    docker build -t pruebat_triduum .
    docker run -p 8000:8000 pruebat_triduum

## Usage
Once the server is running, navigate to http://127.0.0.1:8000/ in your web browser to access the search page. Enter a query in the search bar and press enter to display the Wikipedia summary.

To generate a search report, enter a query in the search bar and click on the "Search Report" button. The search report will display the number of searches for the given query, the first and last search result, and the number of search results for the most recent search.

## Technologies Used
Django Rest Framework
HTML
MongoDB (Atlas)
CSS
## Authors
### Miguel Angel Restrepo Tangarife - Mirestrepot