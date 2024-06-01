from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_summary, name="cart_summary"),
    path('add/', views.cart_add, name="cart_add"),
    path('remove/', views.cart_remove, name="cart_remove"),
    path('update/', views.cart_update, name="cart_update"),

]