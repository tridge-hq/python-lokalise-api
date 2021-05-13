u"""
lokalise.collections.queued_processes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing queued processes collection.
"""

from __future__ import absolute_import
from .base_collection import BaseCollection
from ..models.queued_process import QueuedProcessModel


class QueuedProcessesCollection(BaseCollection):
    u"""Describes queued processes.
    """
    DATA_KEY = u"processes"
    MODEL_KLASS = QueuedProcessModel
