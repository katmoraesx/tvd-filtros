# front/characters-tvd/Dockerfile

# Etapa de build
FROM node:18 AS build
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    cargo
    
COPY . .
RUN yarn install
RUN yarn build

###autosave

# Etapa de produção (Nginx)
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

