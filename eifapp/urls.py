from django.urls import path
from .views import *


app_name = 'eifapp'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about-us', about, name='about-us'),
    path('sermons', sermons, name='sermons'),
    path('devotionals', devotionals, name='devotionals'),
    path('contact-us', contact, name='contact-us'),
]
