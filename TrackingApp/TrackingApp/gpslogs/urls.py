from django.urls import path
from . import views

urlpatterns = [
    path('', views.gettrack,name='command'),
    path('logs/', views.posttrack,name='data'),

]