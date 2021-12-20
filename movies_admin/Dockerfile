FROM python:3.9

WORKDIR /code
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip \
    && pip3 install -r /code/requirements.txt --no-cache-dir
COPY . .
# COPY entrypoint.sh /home/docker/entrypoint.sh
# CMD ['/home/docker/entrypoint.sh']
# CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000