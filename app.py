from flask import Flask,jsonify, make_response, request
from flask_json_schema import JsonSchema, JsonValidationError
from ml_movie import Recommerder
from flask_cors import CORS
from schema import MOVIE_REQUEST_SCHEMA
recommender = Recommerder()

app = Flask('recommender-movie-upc')
schema = JsonSchema(app)
cors = CORS(app)



@app.errorhandler(JsonValidationError)
def validation_error(e):
    return make_response(jsonify({ 'error': e.message, 'errors': [validation_error.message for validation_error  in e.errors]}),400)

@app.route('/',methods=['GET'])
def ping():
        return "Ping Recommeder Movie App .."


@app.route('/api/v1/movies',methods=['GET'])
def list_movies_all():
    return recommender.list_movies_all()

@app.route('/api/v1/movies/recommeder',methods=['POST'])
@schema.validate(MOVIE_REQUEST_SCHEMA)
def recommerder_movie():
    request_body = request.get_json()
    n_top=5   
    if 'ntop' in request_body:
         n_top = request_body['ntop']   

    movie_id  =  request_body['movieId']  
    response = recommender.recommender_movie(movie_id,n_top)
    return jsonify(response)

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Resource Not Found'), 404)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=9090)

