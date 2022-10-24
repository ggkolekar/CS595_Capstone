from ast import keyword
from django.shortcuts import get_object_or_404, render, redirect
from .models import Listing
from .forms import ListingForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices,state_choices

# Create your views here.

# CRUD - create, retrieve, update, delete, list

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published= True)
  
  paginator = Paginator(listings, 2)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)
    
  context = {
    'listings': listings
    
  }
    
  return render(request, 'listings/listings.html', context)
    
def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)
    
  context = {
        'listing': listing
    }
    
  return render(request, 'listings/listing.html', context)
    
def search(request):
  queryset_list = Listing.objects.order_by('-list_date')
  
  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)
      
  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)
      
  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)
      
  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
      
  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)  
     
    
  context= {
    'state_choices': state_choices,
    'bedroom_choices' : bedroom_choices,
    'price_choices' : price_choices,
    'listings': queryset_list,
    'values': request.GET
  }
    
  return render(request, 'listings/search.html', context)

# to fetch list
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)

# to fetch 1 specific houseobj. from list by id
def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)

# to add new houseobj.
def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        #print(request.POST)
        if form.is_valid():
            # TODO
            form.save()
            return redirect("/")
        
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)

# to edit houseobj
def listing_update(request, pk):
    #form = ListingForm()
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        #print(request.POST)
        if form.is_valid():
            # TODO
            form.save()
            return redirect("/")
        
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)

# to delete houseobj.
def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")
     

    
    
