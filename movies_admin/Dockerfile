FROM python:3.9

WORKDIR /code
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip \
    && pip3 install -r /code/requirements.txt --no-cache-dir
EXPOSE 5432 5432
COPY . .