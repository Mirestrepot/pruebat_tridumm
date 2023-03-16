from pymongo import MongoClient

client = MongoClient('mongodb+srv://mirestrepot:Y34589ok.@twitterapi.tixzlnu.mongodb.net/?retryWrites=true&w=majority')
db = client['prueba-tecnica']
db_colection = db['buscador_latino_search']