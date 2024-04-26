from django.urls import path
from .views import register, CustomLoginView, CustomLogoutView, profile
#* http://127.0.0.1:8000/accounts/register
#* http://127.0.0.1:8000/accounts/home
#* http://127.0.0.1:8000/accounts/logout
#* http://127.0.0.1:8000/accounts/login
#* http://127.0.0.1:8000/accounts/profile

urlpatterns = [
    path('register/', register, name='register'),
    # path('home/', home, name='home' ),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout" ),
    path('profile', profile, name='profile')
    # path('home/'),
]
