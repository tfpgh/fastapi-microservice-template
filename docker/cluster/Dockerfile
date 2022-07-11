FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./docker-cluster-requirements.txt /code/docker-cluster-requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/docker-cluster-requirements.txt

COPY ./app /code/app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
