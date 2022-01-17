FROM mongo

COPY weather_db /home/weather_db
COPY mongo.sh /home/mongo.sh
RUN chmod 777 /home/mongo.sh

CMD /home/mongo.sh