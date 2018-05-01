from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
# Create your models here.

class OwnerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    addresss = models.CharField(max_length=150)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    country = models.CharField(max_length=100)

    def create_profile(sender,**kwargs):
        if kwargs['created']:
            owner_profile = OwnerProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile,sender=User)

    def __str__(self):
        return self.user.username

class VehicleMake(models.Model):
    make_id = models.IntegerField()

    make_name = models.CharField(max_length=100)

    def __str__(self):
        return self.make_name

class VehicleDetail(models.Model):
    owner = models.OneToOneField(OwnerProfile,on_delete=models.CASCADE)

    chasis_no = models.CharField(max_length=17)

    licence_plate_no = models.CharField(max_length=7)

    vehicle_make = models.ForeignKey(VehicleMake,on_delete=models.CASCADE)
    
    date_registered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.licence_plate_no