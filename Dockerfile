FROM python:3.9.1-alpine3.12
ENV PYTHONUNBUFFERED=1
COPY /src/requirements.txt /code/
RUN apk add --update --no-cache bash postgresql-dev libffi-dev \
    gcc g++ curl-dev libressl-dev musl-dev binutils gdal-dev geos-dev make && \
    pip install --upgrade pip
RUN pip install -r /code/requirements.txt
COPY ./src /code/
WORKDIR /code



