#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.test import TestCase
from rest_framework.authtoken.models import Token

from .models import User


class UserTests(TestCase):

    def test_user_creation(self):
        """Create a new user."""
        user = User()
        user.save()
        token = Token.objects.get(user=user)
        assert token is not None
        assert len(token.key) == 40

    def test_user_group(self):
        """Make sure user groups are created properly."""
        user = User()
        user.save()
        user.add_group('free')
        assert len(user.groups.all()) == 1
        assert user.groups.all()[0].name == 'free'
