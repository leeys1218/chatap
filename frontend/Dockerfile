FROM node:16.17.0

WORKDIR ./

COPY . .
COPY ./package*.json ./

RUN npm install
RUN npm run build

CMD ["npm", "run", "dev"]


