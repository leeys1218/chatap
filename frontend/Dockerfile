FROM node:14-alpine

WORKDIR ./frontend

COPY . .

RUN cd frontend && ls
RUN cd frontend && npm install --silent
RUN npm run build

CMD ["npm", "run", "dev"]


