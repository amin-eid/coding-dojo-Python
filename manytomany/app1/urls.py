from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook', views.addbook),
    path('books/<int:id>', views.viewbook),
    path('pubtobook/<int:id>', views.pubtobook),
]