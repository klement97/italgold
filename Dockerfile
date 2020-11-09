FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev
RUN apk add postgresql postgresql-dev && pip install psycopg2
RUN apk add jpeg-dev zlib-dev libjpeg && pip install Pillow
RUN apk del build-deps

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

# create the app user
RUN addgroup -S app && adduser -S app -G app

# chown all the files to the app user
RUN chown -R app:app /code/

# change to the app user
USER app
