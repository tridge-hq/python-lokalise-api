u"""
lokalise.models.file
~~~~~~~~~~~~~~~~~~~~
Module containing file model.
"""

from .base_model import BaseModel


class FileModel(BaseModel):
    u"""Describes file.
    """
    ATTRS = [
        u'filename',
        u'key_count'
    ]