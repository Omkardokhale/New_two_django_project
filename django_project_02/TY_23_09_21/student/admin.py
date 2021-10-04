from django.contrib import admin
from .models import Country,State,City

# admin.site.register(City)
# admin.site.register(Country)
# admin.site.register(State)




class CountryAdmin(admin.ModelAdmin):


    list_display  = ['name','population']
    search_fields = ['name','population']

admin.site.register(Country,CountryAdmin)




class StateAdmin(admin.ModelAdmin):

    list_display  = ['name','population']
    search_fields = ['name','population']

admin.site.register(State,StateAdmin)




class CityAdmin(admin.ModelAdmin):


    list_per_page = 10

    list_display  = ['city_name','country','population']
    search_fields = ['city_name','country']

admin.site.register(City,CityAdmin)




