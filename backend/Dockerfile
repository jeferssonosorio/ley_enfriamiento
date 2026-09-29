FROM python:3.6-alpine AS build-env

ENV LANG=es_CO.UTF-8
ENV LC_ALL=es_CO.UTF-8
ENV LC_CTYPE=es_CO.UTF8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8
ENV DJANGO_SETTINGS_MODULE=config.settings.produccion

RUN apk add --no-cache tzdata
ENV TZ America/Bogota

RUN apk --update --no-cache add \
    build-base \
    mariadb-dev

ARG requirements
COPY ./requirements /tmp/requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/$requirements


FROM build-env
WORKDIR /app
COPY ./ /app
EXPOSE 8000
