u"""
lokalise.request
~~~~~~~~~~~~~~~~
This module sends HTTP requests, parses responses, and returns formatted data.

Attributes:

    :attribute str BASE_URL: path to the Lokalise APIv2.
    :attribute list PAGINATION_HEADERS: list of response headers that contain pagination data.
"""
from __future__ import absolute_import
from typing import Any, Optional, Dict, NoReturn
import json
import requests
from lokalise import errors
import lokalise.client
from ._version import __version__


BASE_URL = u"https://api.lokalise.com/api2/"
PAGINATION_HEADERS = [
    u"x-pagination-total-count",
    u"x-pagination-page-count",
    u"x-pagination-limit",
    u"x-pagination-page"
]


def get(client, path,
        params = None):
    u"""Performs GET requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.get(__prepare(BASE_URL + path),
                                     params=params,
                                     **options(client)))


def post(client, path,
         params = None):
    u"""Performs POST requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.post(__prepare(BASE_URL + path),
                                      data=__format_params(params),
                                      **options(client)))


def put(client, path,
        params = None):
    u"""Performs PUT requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.put(__prepare(BASE_URL + path),
                                     data=__format_params(params),
                                     **options(client)))


def patch(client, path,
          params = None):
    u"""Performs PATCH requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.patch(__prepare(BASE_URL + path),
                                       data=__format_params(params),
                                       **options(client)))


def delete(client, path,
           params = None):
    u"""Performs DELETE requests

    :param client: Lokalise API client
    :type client: lokalise.Client
    :param path: Relative path to the API endpoint
    :param params: Other request params
    :rtype dict:
    """
    return respond_with(requests.delete(__prepare(BASE_URL + path),
                                        data=__format_params(params),
                                        ** options(client)))


def respond_with(response):
    u"""Converts the response data to JSON and attaches pagination-related data.
    An exception will be raised if the response status code is 4xx or 5xx,
    or contains an "error" key

    :param response: Response from the API
    :rtype dict:
    """
    data = response.json()

    if response.status_code > 399 or u"error" in data:
        respond_with_error(data, response.status_code)

    result = {}
    for dict_ in (data, extract_headers_from(response)):
        result.update(dict_)
    return result


def respond_with_error(data, code):
    u"""Raises an error based on the HTTP status code.
    If the status code is unknown, raises a generic ClientError

    :param data: Response body from the API that usually contains error message
    :param code: Response status code
    """
    msg = data[u'error'][u'message']

    if code in errors.ERROR_CODES:
        raise errors.ERROR_CODES[code](msg, code)

    raise errors.ClientError(msg, code)


def extract_headers_from(response):
    u"""Fetches pagination-related data from the response headers

    :param response: Response from the API
    :rtype dict:
    """
    return {
        u"_pagination": dict((
            k.lower(), v) for k,
            v in response.headers.items() if k.lower() in PAGINATION_HEADERS)
    }


def options(client):
    u"""Prepares proper request options, including Accept headers, API token,
    and timeouts.

    :param client: Lokalise API client
    :type client: lokalise.Client
    :rtype dict:
    """
    headers = {
        u"Accept": u"application/json",
        u"User-Agent": u"python-lokalise-api plugin/{__version__}".format(__version__=__version__),
        u"X-Api-Token": client.token,
    }
    return {
        u"timeout": (client.connect_timeout, client.read_timeout),
        u"headers": headers
    }


def __format_params(params = None):
    u"""Converts request params to JSON
    """
    return json.dumps(params) if params else None


def __prepare(path):
    u"""Prepares the URI by stripping all unnecessary slashes
    """
    return path.strip(u'/')
