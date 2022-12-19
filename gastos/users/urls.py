from django.urls import path
from .views import SignUpView, SignInView, LogOut
urlpatterns = [
    path('register', SignUpView.as_view(), name='register'),
    path('login', SignInView.as_view(), name='login'),
    path('logout', LogOut.as_view(), name='logout')
]