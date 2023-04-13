from django.urls import path
from . import views
urlpatterns = [
    path('',views.method1 ),
    path('form',views.form ),
    path('addteacher',views.tadd ),
    path('addstudent',views.sadd ),


]