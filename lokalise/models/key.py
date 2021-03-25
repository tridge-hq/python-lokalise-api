u"""
lokalise.models.key
~~~~~~~~~~~~~~~~~~~
Module containing key model.
"""

from __future__ import absolute_import
from .base_model import BaseModel


class KeyModel(BaseModel):
    u"""Describes key model.
    """
    DATA_KEY = u'key'

    ATTRS = [
        u'key_id',
        u'created_at',
        u'created_at_timestamp',
        u'key_name',
        u'filenames',
        u'description',
        u'platforms',
        u'tags',
        u'comments',
        u'screenshots',
        u'translations',
        u'is_plural',
        u'plural_name',
        u'is_hidden',
        u'is_archived',
        u'context',
        u'base_words',
        u'char_limit',
        u'custom_attributes',
        u'modified_at',
        u'modified_at_timestamp',
        u'translations_modified_at',
        u'translations_modified_at_timestamp'
    ]
