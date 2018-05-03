from django.contrib.auth.models import User
from rest_framework import serializers
from vehicleapp.models import VehicleDetail,VehicleMake,OwnerProfile

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (('url', 'username', 'email', 'groups'))

class VehicleDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleDetail
        fields = ('owner','chasis_no','licence_plate_no',
                  'vehicle_make','date_registered')

                

class VehicleMakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleMake
        fields = ('make_id','make_name')

        #@action(methods=['delete'], detail=True)
        
class OwnerProfileSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OwnerProfile
        fields = ('user','address','phone_number','country')