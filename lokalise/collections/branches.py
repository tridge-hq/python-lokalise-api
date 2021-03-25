u"""
lokalise.collections.branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing branches collection.
"""

from __future__ import absolute_import
from .base_collection import BaseCollection
from ..models.branch import BranchModel


class BranchesCollection(BaseCollection):
    u"""Describes project branches.
    """
    DATA_KEY = u"branches"
    MODEL_KLASS = BranchModel
