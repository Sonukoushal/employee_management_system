from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.welcome),
    path('admin/',admin.site.urls),
    path('employees/', views.employee_list),
    path('employees/<int:pk>/', views.employee_detail),
]
