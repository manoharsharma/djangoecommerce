import django
from django.urls import path

from .views import *

app_name = 'home'
urlpatterns = [
    django.urls.path('', HomeView.as_view(), name='home'),
    django.urls.path('subcategory/<slug>', SubCategoryView.as_view(), name='subcategory'),
    django.urls.path('detail/<slug>', ItemDetailView.as_view(), name='detail'),
]