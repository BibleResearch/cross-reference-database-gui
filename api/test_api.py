#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase

from .api_test_utility import get_user_token


class UserAPITests(APITestCase):

    def setUp(self):
        self.token = get_user_token()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_users_list(self):
        """."""
        response = self.client.get('/api/v1/users/')
        print(response.data)
        assert response.status_code == 200
        assert len(response.data) == 1


class UnauthenticatedRequests(APITestCase):
    """Make sure unauthenticated requests are handled properly."""

    def test_unauthenticated_request(self):
        response = self.client.get('/api/v1/users/')
        assert response.status_code == 401
