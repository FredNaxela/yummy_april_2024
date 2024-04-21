from django.shortcuts import render
from django.http import HttpResponse
from .models import DishCategory, Dish, Events, Staff, Gallery, ContactInfo


# Create your views here.
def index(request):
    contact_info = ContactInfo.objects.create(
        address='A108 Adam Street, New York, NY 535022',
        email='contact@example.com',
        phone='+1 5589 55488 55',
        opening_hours='Mon-Sat: 11AM - 23PM; Sunday: Closed'
    )

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