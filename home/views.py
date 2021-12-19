from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from .models import *


class BaseView(View):
    views = {}
    views['category'] = Category.objects.all()
    views['subcategory'] = SubCategory.objects.all()


class HomeView(BaseView):
    def get(self, request):
        # self.views['items'] = Item.object.all()
        self.views['items'] = Item.objects.filter(stock='In Stock')
        self.views['ads'] = Ad.objects.all()
        self.views['sliders'] = Slider.objects.all()
        return render(request, 'index.html', self.views)

class SubCategoryView(BaseView):
    def get(self, request, slug):
        self.views['category'] = Category.objects.all()
        self.views['subcategory'] = Item.objects.filter(slug=slug)
        ids = SubCategory.ojbects.get(slug=slug).id
        self.views['subcategory'] = Item.objects.filter(subcategory_id=ids)
        return render(request, 'kitchen.html', self.views)

class ItemDetailView(BaseView):
    def get(self, request, slug):
        self.views['category'] = Category.objects.all()
        self.views['subcategory'] = Item.objects.filter(slug=slug)
        self.views['item detail'] = Item.objects.filter(slug=slug)
        return render(request, 'single.html', self.views)
