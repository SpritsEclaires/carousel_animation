# Generated by Django 4.2.4 on 2023-08-03 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0002_carouselitem_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselitem',
            name='order',
            field=models.CharField(default=5, max_length=4),
        ),
    ]