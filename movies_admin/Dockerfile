FROM python:3.9

WORKDIR /code

COPY requirements.txt .
RUN python3 -m pip install --upgrade pip \
    && pip3 install -r /code/requirements.txt --no-cache-dir
COPY . .
RUN python manage.py collectstatic --noinput
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000