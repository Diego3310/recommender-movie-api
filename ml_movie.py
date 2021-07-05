from load import Load
loadDM = Load()
from pandas.api.types import CategoricalDtype
from scipy.sparse import csr_matrix

class Recommerder:
    def __init__(self):
        self.df_ratings = loadDM.loadDataFrameRatings()
        self.df_movies = loadDM.loadDataFrameMovies()
        self.model = loadDM.loadModel()
    
    def create_csr_matrix(self):

        movie_categ = CategoricalDtype(sorted(self.df_ratings['movieId'].unique()),ordered=True)
        user_categ = CategoricalDtype(sorted(self.df_ratings['userId'].unique()),ordered=True)

        row_matrix = self.df_ratings['movieId'].astype(movie_categ).cat.codes
        col_matrix = self.df_ratings['userId'].astype(user_categ).cat.codes

        ratings = self.df_ratings['rating'].values

        matrix = csr_matrix((ratings,(row_matrix,col_matrix)),shape=(movie_categ.categories.size,
                                            user_categ.categories.size))
        return movie_categ,matrix
    
    def recommender_movie(self,movie_id,n_top):
        
        movie_categ,matrix = self.create_csr_matrix()


        query_index = movie_categ.categories.get_loc(movie_id)
        print('Movie Id: {0} - Matrix index: {1}'.format(movie_id,query_index))
        
        query_vector = matrix[query_index]
        n_top += 1


        print('Inicializando Modelo...')
        distances, indices = self.model.kneighbors(query_vector, n_neighbors= n_top)
        print('Resultados : Distancia:{0} - Indices: {1}'.format(distances,indices))


        response = {'source':{},'recommerders':[]}

        for i in range(0,len(distances.flatten())):
            if i == 0:
            
                movie = self.df_movies[self.df_movies['movieId']==movie_id]
                print('Recommendations for {0}:\n'.format(movie['title'].values))
                
                response['source'] = {
                    "id": str(movie['movieId'].values[0]),
                    "title": movie['title'].values[0],
                    "genres": movie['genres'].values[0]
                }

            else:
                idx = movie_categ.categories[indices.flatten()[i]]
                
                #Obtener Pelicula recomendada
                movie = self.df_movies[self.df_movies['movieId']==idx]
        
                #Calcular distancia
                movie_dist = distances.flatten()[i] *100

                response['recommerders'].append({
                    "id": str(movie['movieId'].values[0]),
                    "position": str(i),
                    "title": movie['title'].values[0],
                    "genres": movie['genres'].values[0],
                    "distance": movie_dist
                })
        return response
    



    