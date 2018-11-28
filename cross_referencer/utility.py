#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Helpful utility functions."""

from .models import BiblePassage


def normalize_bible_passage(bible_passage):
    """Normalize the given bible passage."""
    # TODO: implement normalization here...
    return bible_passage


def create_bible_reference(bible_passage):
    """Create or find the bible passage object corresponding to the given passage."""
    normalized_reference = normalize_bible_passage(bible_passage)
    new_bible_passage, created = BiblePassage.objects.update_or_create(reference=normalized_reference)
    return new_bible_passage
