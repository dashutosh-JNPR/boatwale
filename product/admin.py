from django.contrib import admin
from .models import Boat, Booking, Tour, TourImage, City, Route

# Register your models here.

admin.site.register(Boat)
admin.site.register(Booking)
admin.site.register(Tour)
admin.site.register(TourImage)
admin.site.register(City)
admin.site.register(Route)