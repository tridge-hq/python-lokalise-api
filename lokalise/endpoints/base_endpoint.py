u"""
lokalise.endpoints.base_endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Endpoint parent class inherited by specific endpoints.
"""
from __future__ import absolute_import
from string import Template
from lokalise.utils import to_list
from .. import request


class BaseEndpoint(object):
    u"""Abstract base class for API endpoints. Endpoints are used to load
    the actual data.

    :attribute PATH: contains the template of the relative URI path to
    the API endpoint, for example:

        projects
        projects/system_languages
        projects/$parent_id/contributors
        projects/$parent_id/keys/$resource_id/comments/$subresource_id

    The actual path is generated using the provided ids.
    """
    PATH = u''

    def __init__(self, client):
        u"""Creates a new endpoint.

        :param client: Lokalise API client
        :type client: lokalise.client.Client
        """
        self.client = client

    def all(self, params = None,
            **ids):
        u"""Loads all items for the given endpoint
        (all projects, all contributors etc).

        :param dict params: Other request parameters like "page" or "limit"
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.get(self.client, path, params)

    def find(self, params = None,
             **ids):
        u"""Loads an item for the given endpoint
        (one project, one contributor etc).

        :param dict params: Other request parameters
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        path = self.path_with_params(**ids)
        return request.get(self.client, path, params)

    def create(self, params = None,
               wrapper_attr = None,
               **ids):
        u"""Creates a new resource for the given endpoint.

        :param dict params: Resource parameters
        :param str wrapper_attr: Attribute to wrap the params into. For example:
            [{"comment": "test"}]
        becomes
            {"comments": [{"comment": "test"}]}
        with the `wrapper_attr` set to "comments"
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        if wrapper_attr and params:
            params = {wrapper_attr: to_list(params)}

        path = self.path_with_params(**ids)
        return request.post(self.client, path, params)

    def update(self, params,
               wrapper_attr = None,
               **ids):
        u"""Updates a resource for the given endpoint.

        :param dict params: Resource parameters
        :param str wrapper_attr: Attribute to wrap the params into
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        if wrapper_attr:
            params = {wrapper_attr: to_list(params)}
        path = self.path_with_params(**ids)
        return request.put(self.client, path, params)

    def delete(self, params = None,
               wrapper_attr = None,
               **ids):
        u"""Deletes a resource for the given endpoint.

        :param dict params: Request parameters
        :param str wrapper_attr: Attribute to wrap the params into
        :param ids: Identifiers for path generation
        :rtype dict:
        """
        if wrapper_attr:
            params = {wrapper_attr: params}
        path = self.path_with_params(**ids)
        return request.delete(self.client, path, params)

    def path_with_params(self, **ids):
        u"""Generates relative path to the endpoint using the template stored
        in PATH and the provided ids. Some or all ids may be omitted depending
        on the actual endpoint.
        """
        defaults = dict(parent_id=u'', resource_id=u'', subresource_id=u'')
        return Template(self.PATH).substitute(defaults, **ids)
