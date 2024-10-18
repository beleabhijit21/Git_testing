from django.urls import path
from . import views

urlpatterns = [
    path('av/', views.addOrder_view)
]
