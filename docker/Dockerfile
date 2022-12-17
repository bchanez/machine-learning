FROM python:3.9

WORKDIR /app

ADD docker/requirements.yml /app
RUN pip install --no-cache-dir --upgrade -r requirements.yml
RUN rm requirements.yml
