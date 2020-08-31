from django.shortcuts import render
from offers.models import OffersAd


def homepage(request):
    posts = OffersAd.objects.all()

    context = {
        'posts':posts
    }

    return render(request,'offers/home.html',context)
