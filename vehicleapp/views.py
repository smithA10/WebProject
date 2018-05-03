from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from vehicleapp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from vehicleapp.forms import RegistrationForm,VehicleRegistrationForm,EditProfileForm
from rest_framework import viewsets
from vehicleapp.serializer import VehicleDetailSerializer,VehicleMakeSerializer,OwnerProfileSerializers,UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
# Create your views here.

def  home(request):
    return render(request,"vehicleapp/home.html")

def  about(request):
    return render(request,"vehicleapp/about.html")

def get_chart(request):
    return render(request,"vehicleapp/charts.html")

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/vehicleapp/home')
    return render(request,'vehicleapp/login.html')

def view_profile(request):
    vehicle_detail = VehicleDetail.objects.all()
    args = {'user': request.user}
    return render(request, 'vehicleapp/profile.html',{
        'vehicle': vehicle_detail
    })
@login_required
def edit_profile(request):
    if request.method =="POST":
        form = EditProfileForm(request.POST,instance=request.user)

        if form.is_valid():

            form.save()
            return redirect('/vehicleapp/home')

        else:
            form = EditProfileForm(instance=request.user)
            return render(request,'vehicleapp/edit_profile.html',{
            'form': form
        })

    form = EditProfileForm(instance=request.user)
    return render(request,'vehicleapp/edit_profile.html',{
        'form': form
    })


# register
def create_account(request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('/vehicleapp/profile')

        else:
            form = RegistrationForm()
            return render(request,'vehicleapp/registration.html',{
            'form': form
        })

    form = RegistrationForm()
    return render(request,'vehicleapp/registration.html',{
        'form': form
    })

@login_required
def register_vehicle(request):
    if request.method =="POST":
        form = VehicleRegistrationForm(request.POST)

        if form.is_valid():

            reg_vehicle = form.save(commit=False)
            reg_vehicle.owner = OwnerProfile.objects.get(user=request.user)
            reg_vehicle.save()
            return redirect('/vehicleapp/home')

        else:
            form = VehicleRegistrationForm()
            return render(request,'vehicleapp/vehicle_reg_form.html',{
            'form': form
        })

    form = VehicleRegistrationForm()
    return render(request,'vehicleapp/vehicle_reg_form.html',{
        'form': form
    })

def get_vehiclemake_range(request, offset, limit):
    offset = int(offset)
    limit = int(limit)
    print(limit)
    vehiclemake = VehicleMake.objects.all()[offset:limit]
    return render(request, 'vehicleapp/listing.html', {
        'vehiclemake': vehiclemake
    })

def get_data(request):
    data = {
        "sales":100,
        "customers": 20,
    }
    return JsonResponse()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class VehicleDetailViewset(viewsets.ModelViewSet):    
    queryset = VehicleDetail.objects.all()
    serializer_class = VehicleDetailSerializer
 

class OwnerProfileViewset(viewsets.ModelViewSet):    
    queryset = OwnerProfile.objects.all()
    serializer_class = OwnerProfileSerializers


class VehicleMakeViewset(viewsets.ModelViewSet):    
    queryset = VehicleMake.objects.all()
    serializer_class = VehicleMakeSerializer

