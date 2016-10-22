from django.contrib import admin
from .models import Booking, Doctor, Profile

admin.site.register(Profile)
class BookingAdmin(admin.ModelAdmin):
	list_display = ['doctor', 'name', 'date', 'start_time', 'email', 'Telephone_number']
	class Meta:
		model = Booking

admin.site.register(Booking, BookingAdmin)

"""
Hall details will be stored in Hall table.
"""
class DoctorAdmin(admin.ModelAdmin):
	list_display = ['doctor', 'Firstname', 'Surname', 'doctor_admin']
	class Meta:
		model = Doctor

admin.site.register(Doctor, DoctorAdmin)
