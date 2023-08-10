from django.db import models

class CarouselItem(models.Model):
    TYPE_CHOICES = (
        ('video', 'Vidéo'),
        ('image', 'Image'),
        ('pdf', 'PDF'),
    )

    title = models.CharField(max_length=100)
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    file = models.FileField(upload_to='carousel_items/')
    sequence = models.CharField(max_length=4, default=5)
    time = models.CharField(max_length=4, default='')