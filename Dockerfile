FROM python:3-slim AS build-env
COPY . /app
WORKDIR /app
RUN apt-get update -qqq && apt-get install pipenv -qqq
RUN pipenv install --system --deploy --ignore-pipfile
CMD ["python", "main.py"]
EXPOSE 4000