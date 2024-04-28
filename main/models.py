from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    is_visible =models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    prepopulated_fields = {'slug': ('name',)}

    def __iter__(self):
        for dish in Dish.objects.filter(category=self, is_visible=True):
            yield dish
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія страв'
        verbose_name_plural = 'Категорії страв'
        ordering = ['sort']

class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True, default='Default Name')
    ingredients = models.TextField(blank=True, null=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
        ordering = ['sort']
    
        
class Events(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    time = models.TimeField()
    photo = models.ImageField(upload_to='events/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подія'
        verbose_name_plural = 'ПодіЇ'
        ordering = ['sort']

    
    
class Staff(models.Model):
    name = models.CharField(max_length=255, default='Default Name')
    position = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
        ordering = ['sort']


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['name']


class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    opening_hours = models.TextField()

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакти'


class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(380)?\d{9,15}$',
                                 message="Number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, validators=[phone_regex])
    date = models.DateField()
    time = models.TimeField()
    count = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ('-date_created',)