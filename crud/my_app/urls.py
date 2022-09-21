from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('user_form/',views.form),
    path('update/<str:pk>',views.update),
    path('update_detail/<str:pk>',views.update_detail),
    path('delete/<str:pk>',views.delete),
]
