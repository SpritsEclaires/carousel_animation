from django import forms
from .models import CarouselItem

class CarouselItemForm(forms.ModelForm):
    class Meta:
        model = CarouselItem
        fields = ['title', 'item_type', 'file', 'time',  'sequence']
        ordering = ('-sequence',)