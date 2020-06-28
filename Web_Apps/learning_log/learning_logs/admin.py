from django.contrib import admin

# Register your models here.

from .models import Topic, Entry
#We import the model from models.py, using a dot in front which tells Django to look in the same directory.

admin.site.register(Topic)
admin.site.register(Entry)
#The code above tells Django to register and manage our own models through the admin site.