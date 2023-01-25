from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.show),
    path('shows/new', views.addshow),
    re_path(r'^shows/add', views.showsadd),
    path('shows/<int:id>', views.show_id),
    path('shows/<int:id>/delete', views.delete),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/edit2', views.edit2),
]