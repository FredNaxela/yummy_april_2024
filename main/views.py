from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DishCategory, Dish, Events, Staff, Gallery, ContactInfo
from .forms import ReservationForm
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True),
        gallery = Gallery.objects.filter(is_visible=True)
        events = Events.objects.all()
        staff = Staff.objects.all()
        contact_info = ContactInfo.objects.first()
        form = ReservationForm()

        context['title_menu'] = 'Check Our <span>Yummy Menu</span>',
        context['title_gallery'] = 'Check <span>Our Gallery</span>',
        context['title_events'] = 'Share <span>Your Moments</span> In Our Restaurant',
        context['title_staff'] = 'Our <span>Proffesional</span> Chefs',
        context['title_contact'] = 'Need Help? <span>Contact Us</span>',
        context['categories'] = categories,
        context['gallery'] = gallery,
        context['events'] = events,
        context['staff'] = staff,
        context['contact_info'] = contact_info,
        context['form'] = form

        return context

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вашe бронювання прийняте!')
            return redirect('main:index')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)

def manager(request):
    ...