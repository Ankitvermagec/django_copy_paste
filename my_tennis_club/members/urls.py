from .import views
from django.urls import path



urlpatterns = [
    path('',views.home,name="Home"),
    path('insert/',views.insert,name="insert"),
    path('update/<int:id>',views.update),
    path('delete/<int:cl>',views.delete),
    
    path('temp/',views.temp,name='temp2'),
    
]
