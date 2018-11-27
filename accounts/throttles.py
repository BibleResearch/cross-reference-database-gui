#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework.throttling import UserRateThrottle


# these throttles are not used... yet (see https://www.django-rest-framework.org/api-guide/throttling/ for more details)


class FreeUserThrottle(UserRateThrottle):
    scope = 'free'


class PaidUserThrottle(UserRateThrottle):
    scope = 'paid'
