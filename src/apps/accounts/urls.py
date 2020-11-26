
# from django.urls import path
# from django.contrib.auth import views as auth_views

# from . import views
# app_name="accounts"
# urlpatterns = [
#     path("", views.index, name="index"),
#     path("login", views.login, name="login"),
#     path("contact", views.contact, name="contact"),
#     path("about", views.about, name="about"),
# ]

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
app_name="accounts"
urlpatterns = [
    path('',views.index,name="home"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    
    # Django Auth
    
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]