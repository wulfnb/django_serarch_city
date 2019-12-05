from django.urls import path
from .views import login_view,logout_view, validate_otp_api, dashboard, signup_view, signup_api, login_api
# SignUpView, 

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signup_api/', signup_api, name='signup_api'),
    path('login/', login_view, name='login'),
    path('login_api/', login_api, name='login_api'),
    path('logout/', logout_view, name='logout'),
    path('validate_otp_api/', validate_otp_api, name='validate_otp_api'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', dashboard, name='dashboard'),
]