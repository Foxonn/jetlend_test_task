##How to right run app

0. `docker-composer up --build`

0. `In container 'app' execution cli 'python jl_app/manage.py makemigrations' 
    and 'python jl_app/manage.py migrate'`

0. `python jl_app/manage.py createsuperuser`

###Documentation
0. http://localhost:8000/swagger/ or http://localhost:8000/redoc/