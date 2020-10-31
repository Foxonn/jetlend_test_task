## How to right run app

1. `docker-composer up --build`

0. `In container 'app' you need executed 'python jl_app/manage.py makemigrations'
    and 'python jl_app/manage.py migrate'`

0. `python jl_app/manage.py createsuperuser`

### Documentation
0. http://localhost:8000/swagger/ or http://localhost:8000/redoc/
