FROM python

COPY ./app/ /app/

RUN pip install pipenv

WORKDIR app

RUN pipenv install --deploy --system --ignore-pipfile

CMD python jl_app/manage.py runserver 0.0.0.0:8000
