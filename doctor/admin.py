from django.contrib import admin
from .models import Dentist, DentistTime,Contact,Appointment

admin.site.register(Dentist)
admin.site.register(DentistTime)
admin.site.register(Contact)
admin.site.register(Appointment)


