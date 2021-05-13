u"""
lokalise.utils
~~~~~~~~~~~~~~
This module contains various utility functions.
"""
from __future__ import absolute_import


def snake_to_camel(word):
    u"""Converts string in snake case to camel case.
    For example, "test_string" becomes "TestString"
    """
    return u''.join(x.capitalize() or u'_' for x in word.split(u'_'))


def to_list(obj):
    u"""Converts an object to a list. If the object is already a list,
    does nothing.

    :param obj: Object to convert
    """
    return obj if isinstance(obj, list) else [obj]
