from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('project_detail/<int:project_id>/', views.project_detail, name='project_detail'),
    path('wendy-home', views.wendy_home, name='wendy-home'),
    path('about', views.about, name='about'),
]