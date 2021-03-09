from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address


class AddressView(CreateView):

    model = Address
    fields = ['address']
    template_name = 'addresses/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoidHVuYWhvYmJ5IiwiYSI6ImNra3IwaDNxcTBtbzAycm81dTFpOWhvcjAifQ.8ixXcuSDUuAlDSlazSLMCA'
        context['addresses'] = Address.objects.all()
        return context