from django.db import models
from django.contrib.auth.models import Permission, User

class Profile(models.Model):
    user = models.ForeignKey(User, default=User)
    Firstname = models.CharField(max_length=250, default='Enter first name name here')
    Surname = models.CharField(max_length=250, default='Enter surname name here')
    first_line_of_address = models.CharField(max_length=250, default='Enter 1st line of address here')
    second_line_of_address = models.CharField(max_length=250, default='Enter 2nd line of address here')
    County = models.CharField(max_length=250, default='Enter your county here')
    City = models.CharField(max_length=250, default='Enter your city here')
    Postcode = models.CharField(max_length=250, default='Enter your postcode here')
    Telephone_number = models.CharField(max_length=250, default='Enter telephone number here')
    profile_pic = models.FileField()
    create = models.BooleanField(default=False)

    def __str__(self):
        return self.Firstname + ' - ' + self.Surname

class Booking(models.Model):
    doctor = models.ForeignKey('Doctor')
    date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    name = models.CharField(max_length=30)
    email = models.EmailField('Email', max_length=30)
    Telephone_number = models.CharField(max_length=250)

    class Meta:
        unique_together = ('doctor', 'date', 'start_time',)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


"""
It contains the information about the Hall, i.e. what is the name of the hall and its other hall featured related
informations.
"""


class Doctor(models.Model):
    doctor = models.ForeignKey(User)
    Firstname = models.CharField(max_length=250)
    Surname = models.CharField(max_length=250)
    doctor_admin = models.EmailField(max_length=40)

    class Meta:
        unique_together = ('doctor', 'doctor_admin')

    def __unicode__(self):
        return self.Surname

    def __str__(self):
        return self.Surname
