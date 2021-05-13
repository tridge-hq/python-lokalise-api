"""
lokalise.endpoints.tasks_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing tasks endpoint.
"""
from __future__ import absolute_import
from .base_endpoint import BaseEndpoint


class TasksEndpoint(BaseEndpoint):
    """Describes tasks endpoint.
    """
    PATH = "projects/$parent_id/tasks/$resource_id"
