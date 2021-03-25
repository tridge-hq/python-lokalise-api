u"""
lokalise.collections.base_collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Collection parent class inherited by specific collections.
"""
from __future__ import absolute_import
from typing import Any, Dict, List
from ..models.base_model import BaseModel


class BaseCollection(object):
    u"""Abstract base class for resources collections.

    :attribute DATA_KEY: contains the key name that should be used to fetch
    collection data. Response usually arrives in the following format:
    {"project_id": "abc", contributors: [{"user_id": 1}, {"user_id": 2}]}
    In this case, the DATA_KEY would be "contributors"

    :attribute MODEL_KLASS: tells which class to use to produce models for each
    item in the collection.

    :attribute COMMON_ATTRS: list of common attributes that the collections may have.
    """
    DATA_KEY = u''
    MODEL_KLASS = BaseModel
    COMMON_ATTRS = [
        u'project_id',
        u'user_id',
        u'branch',
        u'errors',
        u'team_id'
    ]

    def __init__(self, raw_data):
        u"""Creates a new collection.
        To get access to collection data, use `items` attribute.
        Pagination-related data is stored inside the following attributes:

            total_count
            page_count
            limit
            current_page

        :param raw_data: Data returned by the API
        """
        self.__extract_common_attrs(raw_data)

        raw_items = raw_data[self.DATA_KEY]
        self.items = []
        for item in raw_items:
            self.items.append(self.MODEL_KLASS(item))  # pylint: disable=E1102

        pagination = raw_data.get(u"_pagination", {})
        if pagination:
            self.total_count = int(pagination.get(
                u"x-pagination-total-count", 0))
            self.page_count = int(pagination.get(u"x-pagination-page-count", 0))
            self.limit = int(pagination.get(u"x-pagination-limit", 0))
            self.current_page = int(pagination.get(u"x-pagination-page", 0))

    def is_last_page(self):
        u"""Checks whether the current collection set is the last page.

        :rtype: bool
        """
        return not self.has_next_page()

    def is_first_page(self):
        u"""Checks whether the current collection set is the first page.

        :rtype: bool
        """
        return not self.has_prev_page()

    def has_next_page(self):
        u"""Checks whether the current collection set has the next page.

        :rtype: bool
        """
        return self.current_page > 0 and self.current_page < self.page_count

    def has_prev_page(self):
        u"""Checks whether the current collection set has the previous page.

        :rtype: bool
        """
        return self.current_page > 1

    def __extract_common_attrs(self, raw_data):
        u"""Fetches common data from the response and sets the
        corresponding attributes.
        """
        for attr in self.COMMON_ATTRS:
            if attr in raw_data:
                setattr(self, attr, raw_data[attr])
