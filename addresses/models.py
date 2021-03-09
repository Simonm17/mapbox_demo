import geocoder

from django.db import models


mapbox_access_token = 'pk.eyJ1IjoidHVuYWhvYmJ5IiwiYSI6ImNra3IwaDNxcTBtbzAycm81dTFpOWhvcjAifQ.8ixXcuSDUuAlDSlazSLMCA'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)

