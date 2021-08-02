from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class AboutForm(UserCreationForm):
    
    class Meta:
        model= About
        fields="__all__"

class BookingForm(UserCreationForm):
    
    class Meta:
        model= Booking
        fields="__all__"
        
class RoomsForm(forms.ModelForm):
    class Meta:
        model=Room
        exclude=['book']
        
class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields="__all__"

class DinningForm(forms.ModelForm):
    class Meta:
        model=Dinning
        fields="__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"