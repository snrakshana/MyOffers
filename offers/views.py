from django.shortcuts import render
from offers.models import OffersAd
from django.core.paginator import Paginator


def homepage(request):
    posts = OffersAd.objects.all()

    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    

    context = {
        'posts':posts,
        
    }

    return render(request,'offers/home.html',context)


def navbar(request):
    return render(request,'offers/navbar.html')