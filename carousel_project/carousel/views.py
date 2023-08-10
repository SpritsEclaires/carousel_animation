from django.shortcuts import render
from .models import CarouselItem
from .forms import CarouselItemForm

def carousel(request):
    items = CarouselItem.objects.all().order_by('sequence')
    return render(request, 'carousel/carousel.html', {'items': items})

