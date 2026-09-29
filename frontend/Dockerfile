#build step 1 (installing node modules and preparing compiled build)
FROM node:22-alpine as develop-stage

WORKDIR /app

COPY package*.json ./

RUN npm i

COPY . .

EXPOSE 5173

CMD npm install && npm run dev -- --host
