FROM python:3.8-slim-buster


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /django





# install psycopg2 dependencies
RUN apt update && apt install -y gcc gunicorn python-gevent python3-dev musl-dev


COPY requirements.txt /django/requirements.txt

RUN pip install -r requirements.txt



# copy project
COPY . .
CMD /usr/local/bin/gunicorn baseproject.wsgi:application -w 2 -b :80

EXPOSE 80