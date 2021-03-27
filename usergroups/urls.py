from django.urls import include, path
from . import views

urlpatterns = [
    path('getgroups', views.get_groups),
    path('associate', views.associate_user_to_group),
    path('getuserdetails', views.get_user_details),
    path('createuser', views.create_user),
    path('creategroup', views.create_group)
]
