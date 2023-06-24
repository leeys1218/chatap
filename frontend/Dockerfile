FROM node:16.17.0

WORKDIR ./frontend

COPY . .

RUN cd frontend && npm install -g npm@9.7.1
RUN cd frontend && npm install
RUN cd frontend && npm run build


CMD cd frontend && npm run dev


