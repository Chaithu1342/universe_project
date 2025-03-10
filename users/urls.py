from django.urls import path
from .views import home, signup, dashboard

urlpatterns = [
    path('', home, name='home'),  # Add this line
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
]
