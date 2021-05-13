u"""
lokalise.collections.files
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing files collection.
"""

from __future__ import absolute_import
from .base_collection import BaseCollection
from ..models.file import FileModel


class FilesCollection(BaseCollection):
    u"""Describes files.
    """
    DATA_KEY = u"files"
    MODEL_KLASS = FileModel
