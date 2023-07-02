FROM python:3.10


WORKDIR /backend

COPY . .

RUN cd backend && pip install -r requirements.txt
RUN cd backend && pip uninstall uvicorn
RUN cd backend && pip install 'uvicorn[standard]'


ENV API_ENV "prod"

CMD cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8080

