FROM python:3.12-alpine

RUN pip install --upgrade pip
WORKDIR /app

COPY ./init_db /app/init_db
COPY ./input /app/input
COPY ./app /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
