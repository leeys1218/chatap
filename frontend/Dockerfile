FROM node:16.17.0

WORKDIR /frontend

COPY package*.json ./
COPY package*.json ./frontend
COPY . ./frontend
COPY . .


RUN npm install
RUN npm run build

CMD ["npm", "run", "dev"]


