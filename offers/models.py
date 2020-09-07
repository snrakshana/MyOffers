from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.core.validators import URLValidator


def upload_location(instance, filename):
    file_path = 'offer/{property_name}/{area}-{filename}'.format(
        area=str(instance.area), property_name=str(instance.property_name), filename=filename)
    return file_path

catergory_choices = (
    ('hotel', 'hotel'),
    ('food', 'food'),
    ('activities','activities'),
    ('clothing','clothing'),
    ('items','items'),
    ('other','other')
)

class OffersAd(models.Model):
    property_name = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=100, null=True)
    url = models.TextField(validators=[URLValidator()])
    category = models.CharField(max_length=100, null=True,choices=catergory_choices)
    description = models.CharField(max_length=1000, null=True)
    image = models.ImageField(upload_to=upload_location, null=True)
    contact_number = models.CharField(null=True, max_length=15)
    date_published = models.DateField(
        auto_now_add=True, verbose_name="date published")
    date_expired = models.DateField(
         verbose_name="date Expired")
    slug = models.SlugField(blank=True, unique=True)
    def __str__(self):
        return f"{self.property_name}-{self.area}-{self.date_published}"






def pre_save_ad_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.property_name + "-" + instance.area)

pre_save.connect(pre_save_ad_post_receiver, sender=OffersAd)