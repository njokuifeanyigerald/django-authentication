from django.urls import path,include
from .views import home, profile,login,logout
urlpatterns = [
    path('', home, name="home"),
    path('profile/', profile, name="profile"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout")
]
