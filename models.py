from django.db import models

class PhotoManager(models.Manager):
    def approved_photos(self):
        return self.filter(approved=True)
    
    def unapproved_photos(self):
        return self.filter(approved=False)

class CountryManager(models.Manager):
    def get_photos(self, country_id):
        return Photo.objects.filter(entity_type='country', entity_id=country_id)

class CityManager(models.Manager):
    def get_photos(self, city_id):
        return Photo.objects.filter(entity_type='city', entity_id=city_id)

class ItemManager(models.Manager):
    def get_photos(self, item_id):
        return Photo.objects.filter(entity_type='item', entity_id=item_id)

class UserManager(models.Manager):
    def get_photos(self, user_id):
        return Photo.objects.filter(entity_type='user', entity_id=user_id)

class Country(models.Model):
    name = models.CharField(max_length=100)
    objects = CountryManager()

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    objects = CityManager()

class Item(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    objects = ItemManager()

class User(models.Model):
    username = models.CharField(max_length=100)
    objects = UserManager()

class Photo(models.Model):
    entity_type_choices = [
        ('country', 'Country'),
        ('city', 'City'),
        ('item', 'Item'),
        ('user', 'User'),
    ]
    entity_type = models.CharField(max_length=10, choices=entity_type_choices)
    entity_id = models.PositiveIntegerField()
    image = models.ImageField(upload_to='photos/')
    approved = models.BooleanField(default=False)
    objects = PhotoManager()
