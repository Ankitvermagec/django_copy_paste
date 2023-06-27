from .import views
from django.urls import path



urlpatterns = [
    path('',views.home,name="Home"),
    path('insert/',views.insert,name="insert"),
]
