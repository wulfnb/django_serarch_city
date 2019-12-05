from django.urls import path, include

urlpatterns = [
    path('country/', include('country.urls')),
    path('', include('users.urls')),
    path('users/', include('users.urls')),
]
