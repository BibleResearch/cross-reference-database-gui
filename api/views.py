#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework import permissions
from rest_framework import generics

from accounts.models import User
from .serializers import UserSerializer


class UserView(generics.ListAPIView):
    """Return a list of all users."""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
