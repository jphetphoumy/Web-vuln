FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w4", "main:app", "--bind", "0.0.0.0:8000"]
