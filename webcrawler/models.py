from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def __unicode__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(Brand)
    model = models.CharField(max_length=200)
    price = models.FloatField()
    license = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.license