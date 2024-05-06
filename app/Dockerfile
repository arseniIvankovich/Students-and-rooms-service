FROM python:3.12-alpine

RUN pip install --upgrade pip
WORKDIR /app

COPY logging.conf .
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
