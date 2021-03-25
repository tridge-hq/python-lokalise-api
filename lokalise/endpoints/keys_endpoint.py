u"""
lokalise.endpoints.keys_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing keys endpoint.
"""
from __future__ import absolute_import
from .base_endpoint import BaseEndpoint


class KeysEndpoint(BaseEndpoint):
    u"""Describes keys endpoint.
    """
    PATH = u"projects/$parent_id/keys/$resource_id"
