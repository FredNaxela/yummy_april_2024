from django.db import models

# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible =models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    
    
class EventCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    
        
class Event(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    
    
class StaffCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    
    
class Staff(models.Model):
    category = models.ForeignKey(StaffCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='staff')


class GalleryCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    
    
class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery')