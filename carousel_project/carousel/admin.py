from django.contrib import admin
from .models import CarouselItem



class CarouselItemAdmin(admin.ModelAdmin):
    icon_name = 'work'
    list_per_page = 50
    model = CarouselItem
    list_filter = ('item_type',)
    search_fields = ('title',)
    list_display = ('item_type', 'title', 'file','time', 'sequence')
    ordering = ('sequence',)


admin.site.register(CarouselItem, CarouselItemAdmin)