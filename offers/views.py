from django.shortcuts import render
from offers.models import OffersAd
from django.core.paginator import Paginator
from offers.filters import OffersFilter


def homepage(request):
    posts = OffersAd.objects.all()

    myfilter = OffersFilter(request.GET, queryset=posts)
    posts = myfilter.qs
    
    
    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        'posts':posts,
        'myfilter':myfilter,
        
    }

    return render(request,'offers/home.html',context)

def slider(request):
    return render(request,"offers/imageslide.html")