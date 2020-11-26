from django.urls import path
from django.contrib.auth import views as auth_views
from src.forms import UserLoginForm
from . import views
app_name="public"
urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="accounts/login.html",
    authentication_form=UserLoginForm), name='login'),

]