## How to right run app

` create empty directory 'db', he needs for postgres`

`docker-compose up --build`

`In container 'app' you need executed 'python jl_app/manage.py makemigrations'
    and 'python jl_app/manage.py migrate'`

`python jl_app/manage.py createsuperuser`

### Documentation
`http://localhost:8000/swagger/` or `http://localhost:8000/redoc/`
