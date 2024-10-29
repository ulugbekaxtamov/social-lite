from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from .forms import CustomUserCreationForm

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput,
        help_text=""
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as before, for verification.")
    )

    class Meta:
        model = User
        fields = ("username", "name")


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post:post_list')
        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return self.request.user
