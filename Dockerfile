FROM python:3.8
WORKDIR /app
COPY ./app/requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
COPY ./app /app