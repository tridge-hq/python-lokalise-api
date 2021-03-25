u"""
lokalise.models.branch
~~~~~~~~~~~~~~~~~~~~~~
Module containing branch model.
"""
from __future__ import absolute_import
from .base_model import BaseModel


class BranchModel(BaseModel):
    u"""Describes project branch model.
    """
    DATA_KEY = u'branch'

    ATTRS = [
        u'branch_id',
        u'name',
        u'created_at',
        u'created_at_timestamp',
        u'created_by',
        u'created_by_email'
    ]
