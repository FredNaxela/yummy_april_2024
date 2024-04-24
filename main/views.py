from django.shortcuts import render
from django.http import HttpResponse
from .models import DishCategory, Dish, Events, Staff, Gallery, ContactInfo


# Create your views here.
def index(request):

    categories = DishCategory.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    events = Events.objects.all()
    staff = Staff.objects.all()
    contact_info = ContactInfo.objects.first()

    context = {
        'title_menu': 'Check Our <span>Yummy Menu</span>',
        'title_gallery': 'Check <span>Our Gallery</span>',
        'title_events': 'Share <span>Your Moments</span> In Our Restaurant',
        'title_staff': 'Our <span>Proffesional</span> Chefs',
        'title_contact': 'Need Help? <span>Contact Us</span>',
        'categories': categories,
        'gallery': gallery,
        'events': events,
        'staff': staff,
        'contact_info': contact_info,
    }

    return render(request, 'main.html', context=context)

def manager(request):
    ...