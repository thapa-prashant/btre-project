from django.shortcuts import get_object_or_404,render
from .models import Listing
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    listings= Listing.objects.order_by('-list_date').filter(is_published=True)
    #paginator set
    paginator=Paginator(listings,2)
    page=request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={
         'listings':paged_listings
     }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    more_info = get_object_or_404(Listing, pk= listing_id)
    context = {
         'listing':more_info
     }
    return render(request,'listings/listing.html',context)

def search(request):

    query_set=Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set= query_set.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set= query_set.filter(city__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_set = query_set.filter(city__lte=bedrooms)

    context={
        'listings':query_set
    }
    return render(request,'listings/search.html',context)
