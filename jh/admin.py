from django.contrib import admin
from .models import *
# Register your models here.

admin.site_header='JHOTEL'
admin.site_title='JHOTEL Admin areas'
admin.site_index_title='Welcome to JHOTEL Admin Area'

admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(Meeting)
admin.site.register(Dinning)
admin.site.register(Contact)
