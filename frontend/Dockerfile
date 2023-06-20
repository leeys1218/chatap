FROM node:14-alpine

WORKDIR ./frontend

COPY . .

RUN cd frontend && ls
RUN cd frontend && npm install --silent
RUN cd frontend && npm run build

CMD ["npm", "run", "dev"]


