from django.db import models

from django.core.validators import URLValidator


def upload_location(instance, filename):
    file_path = 'offer/{property_name}/{area}-{filename}'.format(
        area=str(instance.area), property_name=str(instance.property_name), filename=filename)
    return file_path


class OffersAd(models.Model):
    property_name = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=100, null=True)
    url = models.TextField(validators=[URLValidator()])
    category = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to=upload_location, null=True)
    date_published = models.DateTimeField(
        auto_now_add=True, verbose_name="date published")
    date_expired = models.DateField(
         verbose_name="date Expired")

    def __str__(self):
        return f"{self.property_name}-{self.area}"
