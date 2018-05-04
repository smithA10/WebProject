from django.urls import path,include
from django.contrib.auth.views import login,logout
from vehicleapp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('ownerprofile',views.OwnerProfileViewset )
router.register('vehiclemake',views.VehicleMakeViewset)
router.register('vehicledetail',views.VehicleDetailViewset)

#app_name = "vehicleapp"
urlpatterns = [
    path('home/',views.home, name="home"),
    path('profile/', views.view_profile, name='view_profile'),
    path('edit-profile/',views.edit_profile,name='edit_profile'),
    path('login/', views.login_user, name='login'),
    path('logout/', logout, {'template_name':'vehicleapp/home.html'}, name="logout"),
    path('registration/', views.create_account, name='create_account'),
    path('vehicle-registration/', views.register_vehicle, name='register_vehicle'),
    path('about/', views.about, name='about'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('chart/api/', include(router.urls)),
    path('chart/',views.get_chart,name="get_chart"),
    #path('listing/offset/(?P<offset>\d+)/limit/(?P<limit>\d+)/', views.get_vehiclemake_range,name="makelist")
    #path('snippets/', views.vehiclemake_list),
    #path('snippets/<int:pk>', views.vehiclemake_detail),
]

