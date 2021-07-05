from flask import Flask,jsonify, make_response, request

from ml_movie import Recommerder
recommender = Recommerder()

app = Flask('recommender-movie-upc')

@app.route('/',methods=['GET'])
def ping():
        return "Ping Recommeder Movie App .."
@app.route('/api/v1/movies/recommeder',methods=['POST'])
def recommerder_movie():
    print(request)
    request_body = request.get_json()

    movie_id  =  request_body['movieId']
    n_top = request_body['ntop']   

    response = recommender.recommender_movie(movie_id,n_top)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9090)

