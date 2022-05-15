from django.contrib import admin
from .models import Plant, Watering, Caretaker
# Register your models here.

admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Caretaker)