from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('make_name')

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['model_name']

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)
