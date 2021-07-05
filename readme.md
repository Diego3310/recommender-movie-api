# Proyecto UPC IA 2021-01 - Recomendación de películas

## Requerimientos
- Python 3.8
- Vscode(Extensiones: Python | Jupyter)

## Inicializar en entorno local

1. Descargar Datasets del siguiente link : https://files.grouplens.org/datasets/movielens/ml-25m.zip
2. Descomprimir ml-25m.zip y guardar los archivos movies.csv y ratings.csv en la carpeta static/data
3. Crear entorno virtual
    - Instalar virtualenv para crear entorno virtual =  pip install virtualenv
    -  Crear entorno virtual = venv env 
    -  Activar entorno virtual  
        - bash(gitbash) = source env/Scripts/activate
        - Linux/mac = source env/bin/activate
        - CMD = Ingresar a la carpeta env/Scripts y ejecutar bat activate
    - Instalar dependencias = pip install -r requirements.txt
4. Crear modelo en el archivo train_model.ipynb
    - Seguir los pasos del jupyter notebook hasta la parte del serializado del modelo
    - Verificar la creación del archivo knn_model.pickle en la carpeta static/model
5. Inicializar server para ejecutar API = python app.py

    - Recursos : 
        - POST http://localhost:9090/api/v1/movies/recommeder  | 
          - Schema : 
                - {movieId:integer:required}  = Id de la película
                - {ntop:integer:optional}     = Cantidad de películas a recomendar (Default 5)


