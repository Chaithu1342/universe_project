from django.urls import path
from .views import home, signup, dashboard, user_login, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
