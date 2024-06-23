# docker/web/Dockerfile
FROM node:18 as build
WORKDIR /web
COPY web .
RUN npm install --registry=https://registry.npmmirror.com -g pnpm \
    && pnpm install --registry=https://registry.npmmirror.com \
    && cp .env.docker .env.production \
    && pnpm build

FROM nginx:alpine
WORKDIR /web
COPY --from=build /web/dist /usr/share/nginx/html
COPY ./docker/web/nginx.conf /etc/nginx/conf.d/fuadmin.conf







