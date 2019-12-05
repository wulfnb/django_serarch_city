from django.urls import path
from .views import get_searched, details
# SignUpView, 

urlpatterns = [
    path('q/<str:key_word>', get_searched, name='country'),
    path('details/<str:code>', details, name='details'),
]