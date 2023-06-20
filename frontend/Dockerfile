FROM node:14-alpine

WORKDIR ./frontend

COPY . .

RUN ls
RUN npm install --silent
RUN npm run build

CMD ["npm", "run", "dev"]


