import django_filters
from offers.models import OffersAd


class OffersFilter(django_filters.FilterSet):
    class Meta:
        model = OffersAd
        fields = ['category']