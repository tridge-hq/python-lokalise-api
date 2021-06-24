u"""
lokalise.collections.tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing tasks collection.
"""

from __future__ import absolute_import
from .base_collection import BaseCollection
from ..models.task import TaskModel


class TasksCollection(BaseCollection):
    u"""Describes tasks.
    """
    DATA_KEY = u"tasks"
    MODEL_KLASS = TaskModel
