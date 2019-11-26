from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.
def index(request):
    listings= Listing.objects.order_by('-list_date').filter(is_published=True)
    context={
        'listings':listings,
    }
    return  render(request,'pages/index.html',context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors= Realtor.objects.all().filter(is_mvp=True)
    context={
        realtors:'realtors',
        mvp_realtors:'mvp_realtors'
    }
    return  render(request,'pages/about.html')

