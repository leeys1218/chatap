FROM node:16.17.0

WORKDIR /

COPY . .

RUN npm install
RUN npm run build

CMD ["npm", "run", "dev"]


