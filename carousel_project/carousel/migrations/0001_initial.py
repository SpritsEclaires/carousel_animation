# Generated by Django 4.2.4 on 2023-08-02 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('item_type', models.CharField(choices=[('video', 'Vidéo'), ('image', 'Image'), ('pdf', 'PDF')], max_length=10)),
                ('file', models.FileField(upload_to='carousel_items/')),
            ],
        ),
    ]
