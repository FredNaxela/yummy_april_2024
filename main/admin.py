from django.contrib import admin
from .models import DishCategory, Dish, Events, Staff, Gallery
from django.utils.safestring import mark_safe

# Register your models here.

admin.site.register(Gallery)

@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_visible', 'sort', 'slug')
    list_editable = ('name', 'is_visible', 'sort', 'slug')
    list_filter = ('is_visible',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'price', 'is_visible', 'sort', 'category')
    list_editable = ('price', 'is_visible', 'sort')
    list_filter = ('category', 'is_visible')
    search_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Dish photo'


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag','name', 'price','date', 'sort')
    list_editable = ('price','date', 'sort')
    list_filter = ('date',)
    search_fields = ('name', 'date')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Event photo'

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'position', 'sort',)
    list_editable = ('position', 'sort')
    list_filter = ('position',)
    search_fields = ('name', 'position',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Staff photo'