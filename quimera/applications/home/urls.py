from django.urls import path

from applications.home import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

]