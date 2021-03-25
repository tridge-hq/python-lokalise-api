u"""
lokalise.collections.keys
~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing keys collection.
"""

from __future__ import absolute_import
from .base_collection import BaseCollection
from ..models.key import KeyModel


class KeysCollection(BaseCollection):
    u"""Describes keys.
    """
    DATA_KEY = u"keys"
    MODEL_KLASS = KeyModel
