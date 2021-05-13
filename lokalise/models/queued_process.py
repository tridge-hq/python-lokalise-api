u"""
lokalise.models.queued_process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing queued process model.
"""

from .base_model import BaseModel


class QueuedProcessModel(BaseModel):
    u"""Describes queued process.
    """
    DATA_KEY = u'process'

    ATTRS = [
        u'process_id',
        u'type',
        u'status',
        u'message',
        u'created_by',
        u'created_by_email',
        u'created_at',
        u'created_at_timestamp',
        u'details'
    ]