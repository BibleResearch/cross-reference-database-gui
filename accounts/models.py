#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


def create_token(user):
    Token.objects.create(user=user)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Add a token to each user account after account is created."""
    if created:
        create_token(instance)


class User(AbstractUser):

    def add_group(self, group_name):
        """Add the user to a group."""
        group, created = UserGroup.objects.update_or_create(name=group_name)
        self.groups.add(group)


class UserGroup(Group):

    def __init__(self, name):
        super(Group, self).__init__()
        # overwrite the name attribute
        self.name = name
