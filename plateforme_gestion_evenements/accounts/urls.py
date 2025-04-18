from django.urls import path, include
from . import views

app_name='accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home/', views.HomeView.as_view(), name='home'),
    path('signup/' , views.SignUpView.as_view() , name ='signup'),
]