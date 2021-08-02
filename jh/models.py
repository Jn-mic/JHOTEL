from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime
from model_utils import Choices



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class About(models.Model):
    image=models.ImageField(upload_to='About',blank=True)
    mission=models.TextField()
    vision=models.TextField()


    def __str__(self):
        return str(self.mission)

    def save_about(self):
        self.save()
    
    def delete_about(self):
        self.delete()

class Booking(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"Booking name")
    num = models.CharField(default='Ksh.5000', max_length=10, verbose_name=u"Booking Amount")
    time = models.DateTimeField(verbose_name=u"Booking Arrival Time")
    brief = models.TextField(max_length=300, verbose_name=u"Booking Information")
    slots = models.IntegerField(default=0, verbose_name=u"Remaining slots")

    def __str__(self):
        return self.name
    
    def save_booking(self):
        self.save()
    
    def delete_about(self):
        self.delete()

    class Meta:
        verbose_name = "Booking Information"
        verbose_name_plural = verbose_name

class Room(models.Model):
    room_name=models.CharField(max_length=20,null=True)
    ROOM_NUMBER = Choices(
        (1, 'RM1', ('RM1')),
        (2, 'RM2', ('RM2')),
        (3, 'RM3', ('RM3')),
        (4, 'RM4',('RM4')),
        )
    room_number = models.PositiveSmallIntegerField(choices=ROOM_NUMBER,default=ROOM_NUMBER.RM1,)
    SELECT = Choices(
        ('RM1', 'superior_room', ('Superior room')),
        (2, 'executive_room', ('Executive room')),
        (3, 'junior_room', ('Junior room')),
        (4, 'presidential_room',('Presidential Suite')),
        (4, 'kings_room',('Kings Suite')),
        )
    room_type = models.PositiveSmallIntegerField(choices=SELECT,default=SELECT.superior_room,)
    book=models.ForeignKey(Booking,on_delete=CASCADE,null=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def __str__(self):
        return  str(self.room_name)

class Meeting(models.Model):
    STATUS = Choices(
        (1, 'first_class', ('First class')),
        (2, 'business_class', ('Business class')),
        (3, 'events', ('Events')),
        )
    status = models.PositiveSmallIntegerField(choices=STATUS,default=STATUS.first_class,)
    booK=models.ForeignKey(Booking,on_delete=CASCADE,null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

    def __str__(self):
        return  str(self.status)

    @classmethod
    def get_meeting(cls):
        meeting=cls.objects.all()
        
        return meeting

    def save_meeting(cls):
        current_user=User
        meeting=cls.objects.all().save()

class Dinning(models.Model):
    gaze_house=models.CharField(max_length=200)
    artisan=models.CharField(max_length=200)
    gallery=models.CharField(max_length=200)
    bar=models.CharField(max_length=200)
    booK=models.ForeignKey(Booking,on_delete=CASCADE,null=True)

    def __str__(self):
        return str(self.bar)

    def save_dinning(self):
        self.save()
    
    def delete_dinning(self):
        self.delete()

    @classmethod
    def get_dinning(cls):
        dinning=cls.objects.all()
        return dinning

class Contact (models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return str(self.name)

    def save_contact(self):
        self.save()
    
    def delete_contact(self):
        self.delete()

    @classmethod
    def get_contact(cls):
        contact=cls.objects.all()
        return contact


