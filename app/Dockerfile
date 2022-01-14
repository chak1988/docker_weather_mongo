FROM ubuntu
RUN apt-get update
RUN apt-get install -y
RUN apt install python3-pip -y
RUN pip3 install flask
RUN pip3 install pytelegrambotapi
RUN pip3 install mongoengine
RUN apt install -y mongodb
WORKDIR /home/docker_weather_bot
COPY . /home/docker_weather_bot
COPY webhook_weather_key.pem /etc/ssl/private/webhook_weather_key.pem
COPY webhook_weather_cert.pem /etc/ssl/certs/webhook_weather_cert.pem
RUN python3 weather_models.py
RUN pip3 install gunicorn
CMD ["gunicorn"  , "--bind", "0.0.0.0:5000", "my_weather_bot:app"]
