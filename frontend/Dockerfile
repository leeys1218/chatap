FROM node:16.17.0

COPY . .

RUN npm init
RUN npm install
RUN npm run build

CMD ["npm", "run", "dev"]


