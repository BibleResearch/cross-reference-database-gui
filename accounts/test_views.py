#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase


class ViewTests(TestCase):
    """View related tests."""

    def test_login_view(self):
        response = self.client.get('/accounts/login/')
        assert response.status_code == 200
        assert "Bible Cross Reference Database" in response.content.decode("utf-8")

    def test_login_view_redirect(self):
        response = self.client.get('/accounts/login')
        assert response.status_code == 301
        self.assertEqual(response.url, "/accounts/login/")

    def test_logout(self):
        response = self.client.get('/accounts/logout/')
        assert response.status_code == 302
        self.assertEqual(response.url, "/")
