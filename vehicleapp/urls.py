from django.urls import path
from django.contrib.auth.views import login,logout
from vehicleapp import views

app_name = "vehicleapp"
urlpatterns = [
    path('home/',views.home, name="home"),
    path('profile/', views.view_profile, name='view_profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', logout, {'template_name':'vehicleapp/logout.html'}, name="logout"),
    path('registration/', views.create_account, name='create_account'),
    path('vehicle-registration/', views.register_vehicle, name='register_vehicle'),
    path('about/', views.about, name='about')
]

