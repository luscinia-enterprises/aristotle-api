FROM python:3-alpine

RUN pip install -U pipenv

WORKDIR /app

COPY Pipfile .
RUN pipenv lock
RUN pipenv install --ignore-pipfile

COPY . .

ENTRYPOINT ["pipenv", "run", "gunicorn", "--bind", ":5000", "app:app"]
