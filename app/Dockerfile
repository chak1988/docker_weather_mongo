FROM python:3.9-slim
RUN apt-get update
RUN apt-get install -y
RUN pip3 install flask
RUN pip3 install pytelegrambotapi
RUN pip3 install mongoengine
RUN mkdir -p /usr/src/application/
WORKDIR /usr/src/application/
COPY . /usr/src/application/
COPY app/webhook_weather_key.pem /etc/ssl/private/webhook_weather_key.pem
COPY app/webhook_weather_cert.pem /etc/ssl/certs/webhook_weather_cert.pem
RUN pip3 install gunicorn
CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "my_weather_bot:app"]
