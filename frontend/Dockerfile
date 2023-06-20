FROM node:14-alpine

COPY . .

RUN cd frontend
RUN npm install
RUN npm run build

CMD ["npm", "run", "dev"]


