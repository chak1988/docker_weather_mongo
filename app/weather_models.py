import mongoengine as me
import os


MONGODB_URL = "mongodb://mongodb/dev"
config = globals()[os.environ['MONGO_DB_ADDR']]
me.connect('weather_db', host = config.MONGODB_URL)

class Gallary(me.Document):
    title = me.StringField(required = True, min_length = 2)
    image = me.FileField(required = True)
    @classmethod
    def get_weather_img(cls, title):
        return cls.objects.get(title = title)

if __name__ == "__main__":
    print(config)
    list_of_images = ['partial_clouds.jpg', 'Sunny_weather.jpg', 'Thunder_clouds.jpeg', 'Thunder_storm.jpg']
    for img in list_of_images:
        with open(f'images/{img}', 'rb') as image:
            photo = Gallary(title = f'{img}')
            photo.image.put(image, content_type = 'image/jpeg')
            photo.save()
