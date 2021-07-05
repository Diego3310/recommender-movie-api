#Importando Librerias
import pandas as pd
import time
import pickle

PATH_RATINGS_DF = './static/data/ratings.csv'
PATH_MOVIES_DF  = './static/data/movies.csv'
PATH_MODEL     = './static/model/knn_model.pickle'

class Load:
    


    def loadDataFrameRatings(self):
        print('Creando Dataframe Ratings....')
        start_ratings_ds = time.time()
        chunk_rating = pd.read_csv(PATH_RATINGS_DF,chunksize=1000000 ,
            usecols=['userId', 'movieId', 'rating'],
            dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})
        end_ratings_ds = time.time()
        df_ratings = pd.concat(chunk_rating)
        print("Dataframe Ratings creado en: ",(end_ratings_ds-start_ratings_ds),"sec")
        return df_ratings

    def loadDataFrameMovies(self):

        print('Creando Dataframe Movies....')
        start_movies_ds = time.time()
        chunk_movie = pd.read_csv(PATH_MOVIES_DF,chunksize=1000000,
            usecols=['movieId', 'title',"genres"],
            dtype={'movieId': 'int32', 'title': 'str',"genres":"str"})
        end_movies_ds = time.time()
        df_movies = pd.concat(chunk_movie)
        print("Dataframe Movies creado en: ",(end_movies_ds-start_movies_ds),"sec")
        return df_movies

    def loadModel(self):
        knn_model = ''
        print('Cargando Modelo.....')
        start_model = time.time()
        with open(PATH_MODEL, "rb") as model:
            knn_model = pickle.load(model)
        end_model = time.time()
        print("Modelo cargado en: ",(end_model-start_model),"sec")
        return knn_model

    