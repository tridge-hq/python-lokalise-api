"""
lokalise.endpoints.branches_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Module containing branches endpoint.
"""
from __future__ import absolute_import
from .base_endpoint import BaseEndpoint
from .. import request


class BranchesEndpoint(BaseEndpoint):
    """Describes project branches endpoint.
    """
    PATH = "projects/$parent_id/branches/$resource_id"

    def merge(self, params, **ids):
        """Merges the specified branch into the target branch.

        :param dict params: Merge parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.post(self.client, path + '/merge', params)