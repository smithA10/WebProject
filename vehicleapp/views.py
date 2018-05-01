from django.shortcuts import render

from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from vehicleapp.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from vehicleapp.forms import RegistrationForm,VehicleRegistrationForm


# Create your views here.
def  home(request):
    return render(request,"vehicleapp/home.html")

def  about(request):
    return render(request,"vehicleapp/about.html")

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