FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

COPY ./requirements.txt /app/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/app/requirements.txt

COPY ./app /app/app
