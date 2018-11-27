#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from rest_framework.authtoken.models import Token

from .forms import RegistrationForm
from .models import create_token


class RegistrationView(generic.View):
    form_class = RegistrationForm
    template_name = "registration/registration.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user.add_group('free')

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, generic.View):
    template_name = "registration/profile.html"

    def get(self, request):
        token = Token.objects.get(user=request.user)
        return render(request, self.template_name, {'token': token})


class NewTokenView(LoginRequiredMixin, generic.View):
    template_name = "registration/profile.html"

    def get(self, request):
        # delete the current token for the user
        token = Token.objects.get(user=request.user)
        token.delete()

        # create a new token for the user
        create_token(request.user)

        messages.info(request, 'New API token created!')

        # redirect to profile page
        return HttpResponseRedirect(reverse('accounts:profile'))
