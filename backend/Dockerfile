FROM python:3.10


WORKDIR /backend

COPY . .

RUN pip install -r requirements.txt

ENV API_ENV "prod"

CMD uvicorn app.main:app --host 0.0.0.0 --port 8080

