from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

@login_required
def index(request):
    return render(request,'accounts/index.html')


