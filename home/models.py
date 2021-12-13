from django.db import models

# Create your models here.
LABELS = (('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('', 'default'))
STOCK = (('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock'))
STATUS = (('active', 'active'), ('inactive', 'inactive'))


class Category(models.Model):
    name = models.CharField(max_length=400)
    slug = models.CharField(max_length=400, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=400)
    slug = models.CharField(max_length=400, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media', null=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    url = models.URLField(blank=True)
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Ad(models.Model):
    title = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    url = models.URLField(blank=True)
    rank = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Item(models.Model):
    name = models.TextField()
    slug = models.CharField(max_length=400, unique=True)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media', null=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    labels = models.CharField(choices=LABELS, max_length=400, blank=True)
    status = models.CharField(choices=STATUS, max_length=400, blank=True)
    stock = models.CharField(choices=STOCK, max_length=400, blank=True)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    name = models.CharField(max_length=400)
    logo = models.ImageField(upload_to='media')
    address = models.TextField()
    phone = models.TextField()

    def __str__(self):
        return self.name