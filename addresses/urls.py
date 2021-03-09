from django.urls import path
from .views import AddressView


urlpatterns = [
    path('', AddressView.as_view(), name='home'),
]