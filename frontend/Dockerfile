FROM node:16.17.0

WORKDIR ./frontend


COPY . ./frontend

RUN cd frontend
RUN npm install
RUN npm run build

CMD ["npm", "run", "dev"]


