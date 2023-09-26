# Melp-EDT
Repositorio para la aplicación Melp

Se deben instalar los requerimientos con el comando:

```pip install -r requirements.txt```

Es necesario instalar la librería geo y [SpatiaLite](https://docs.djangoproject.com/en/4.2/ref/contrib/gis/install/spatialite/)

Para poblar la base de datos y correr correctamente el proyecto se deben ejecutar los comandos:

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runscript load_restaurants`

Por último para levantar el servidor es necesario ejecutar el comando:

`python manage.py runserver`

