FROM python:3.10


WORKDIR /backend

COPY . .


RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
RUN pip install uvicorn

ENV API_ENV "prod"

CMD cd backend && uvicorn main:app --host 0.0.0.0 --port 8080

