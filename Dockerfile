FROM mongo:4.4.12-rc1-focal

COPY weather_db /home/weather_db
COPY mongo.sh /home/mongo.sh
RUN chmod 777 /home/mongo.sh

CMD /home/mongo.sh