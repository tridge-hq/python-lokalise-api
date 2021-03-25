u"""
lokalise.client
~~~~~~~~~~~~~~~
This module contains API client definition.
"""
from __future__ import absolute_import
from typing import Any, Optional, Union, Dict, Callable, List
import importlib
from lokalise.utils import snake_to_camel
# from .collections.branches import BranchesCollection
# from .collections.comments import CommentsCollection
# from .collections.contributors import ContributorsCollection
# from .collections.files import FilesCollection
from .collections.keys import KeysCollection
# from .collections.languages import LanguagesCollection
# from .collections.orders import OrdersCollection
# from .collections.payment_cards import PaymentCardsCollection
# from .collections.projects import ProjectsCollection
# from .collections.queued_processes import QueuedProcessesCollection
# from .collections.snapshots import SnapshotsCollection
# from .collections.screenshots import ScreenshotsCollection
# from .collections.tasks import TasksCollection
# from .collections.teams import TeamsCollection
# from .collections.team_users import TeamUsersCollection
# from .collections.team_user_groups import TeamUserGroupsCollection
# from .collections.translations import TranslationsCollection
# from .collections.translation_providers import TranslationProvidersCollection
# from .collections.translation_statuses import TranslationStatusesCollection
# from .collections.webhooks import WebhooksCollection
# from .models.branch import BranchModel
# from .models.comment import CommentModel
# from .models.contributor import ContributorModel
# from .models.key import KeyModel
# from .models.language import LanguageModel
# from .models.order import OrderModel
# from .models.payment_card import PaymentCardModel
# from .models.project import ProjectModel
# from .models.queued_process import QueuedProcessModel
# from .models.snapshot import SnapshotModel
# from .models.screenshot import ScreenshotModel
# from .models.task import TaskModel
# from .models.team_user import TeamUserModel
# from .models.team_user_group import TeamUserGroupModel
# from .models.translation import TranslationModel
# from .models.translation_provider import TranslationProviderModel
# from .models.translation_status import TranslationStatusModel
# from .models.webhook import WebhookModel


class Client(object):
    u"""Client used to send API requests.

    Usage:

        import lokalise
        client = lokalise.Client('api_token')
        client.projects()
    """

    def __init__(self,
                 token,
                 connect_timeout = None,
                 read_timeout = None):
        u"""Instantiate a new Lokalise API client.

        :param str token: Your Lokalise API token.
        :param connect_timeout: (optional) Server connection timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        :type connect_timeout: int or float
        :param read_timeout: (optional) Server read timeout
        (the value is in seconds). By default, the client will wait indefinitely.
        :type read_timeout: int or float
        """
        self.token = token
        self.connect_timeout = connect_timeout
        self.read_timeout = read_timeout

    # def reset_client(self):
        # u"""Resets the API client by clearing all attributes.
        # """
        # self.token = u''
        # self.connect_timeout = None
        # self.read_timeout = None
        # self.__clear_endpoint_attrs()

    # # === Endpoint methods ===
    # def branches(self,
                 # project_id,
                 # params = None
                 # ):
        # u"""Fetches all branches for the given project.

        # :param str project_id: ID of the project to fetch branches for.
        # :param dict params: (optional) Pagination params
        # :return: Collection of branches
        # """
        # raw_branches = self.get_endpoint(u"branches"). \
            # all(parent_id=project_id, params=params)
        # return BranchesCollection(raw_branches)

    # def branch(self,
               # project_id,
               # branch_id):
        # u"""Fetches a single branch.

        # :param str project_id: ID of the project
        # :param branch_id: ID of the branch to fetch
        # :type branch_id: int or str
        # :return: Branch model
        # """
        # raw_branch = self.get_endpoint(u"branches"). \
            # find(parent_id=project_id, resource_id=branch_id)
        # return BranchModel(raw_branch)

    # def create_branch(self,
                      # project_id,
                      # params
                      # ):
        # u"""Creates a new branch inside the project

        # :param str project_id: ID of the project
        # :param dict params: Branch parameters
        # :return: Branch model
        # """
        # raw_branch = self.get_endpoint(u"branches"). \
            # create(params=params, parent_id=project_id)

        # return BranchModel(raw_branch)

    # def update_branch(self,
                      # project_id,
                      # branch_id,
                      # params):
        # u"""Updates a branch.

        # :param str project_id: ID of the project
        # :param branch_id: ID of the branch to update
        # :type branch_id: int or str
        # :param dict params: Update parameters
        # :return: Branch model
        # """
        # raw_branch = self.get_endpoint(u"branches"). \
            # update(params=params, parent_id=project_id, resource_id=branch_id)
        # return BranchModel(raw_branch)

    # def delete_branch(self, project_id,
                      # branch_id):
        # u"""Deletes a branch.

        # :param str project_id: ID of the project
        # :param branch_id: ID of the branch to delete
        # :type branch_id: int or str
        # :return: Dictionary with project ID and "branch_deleted" set to True
        # :rtype dict:
        # """
        # response = self.get_endpoint(u"branches"). \
            # delete(parent_id=project_id, resource_id=branch_id)
        # return response

    # def merge_branch(self, project_id,
                     # branch_id,
                     # params = None
                     # ):
        # u"""Merges a branch.

        # :param str project_id: ID of the project
        # :param branch_id: ID of the source branch
        # :type branch_id: int or str
        # :param dict params: Merge parameters
        # :return: Dictionary with project ID, "branch_merged" set to True, and branches info
        # :rtype dict:
        # """
        # response = self.get_endpoint(u"branches"). \
            # merge(params=params, parent_id=project_id, resource_id=branch_id)
        # response[u'branch'] = BranchModel(response[u'branch'])
        # response[u'target_branch'] = BranchModel(response[u'target_branch'])
        # return response

    # def project_comments(self,
                         # project_id,
                         # params = None
                         # ):
        # u"""Fetches all comments for the given project.

        # :param str project_id: ID of the project to fetch comments for.
        # :param dict params: (optional) Pagination params
        # :return: Collection of comments
        # """
        # raw_comments = self.get_endpoint(u"project_comments"). \
            # all(parent_id=project_id, params=params)
        # return CommentsCollection(raw_comments)

    # def key_comments(self,
                     # project_id,
                     # key_id,
                     # params = None
                     # ):
        # u"""Fetches all comments for the given key inside a project.

        # :param str project_id: ID of the project
        # :param key_id: ID of key to fetch comments for
        # :type key_id: int or str
        # :param dict params: (optional) Pagination params
        # :return: Collection of comments
        # """
        # raw_comments = self.get_endpoint(u"key_comments"). \
            # all(params=params, parent_id=project_id, resource_id=key_id)
        # return CommentsCollection(raw_comments)

    # def key_comment(self,
                    # project_id,
                    # key_id,
                    # comment_id
                    # ):
        # u"""Fetches a single comment for a given key.

        # :param str project_id: ID of the project
        # :param key_id: ID of key to fetch comments for
        # :type key_id: int or str
        # :param comment_id: Comment identifier to fetch
        # :type comment_id: int or str
        # :return: Comment model
        # """
        # raw_comment = self.get_endpoint(u"key_comments").find(
            # parent_id=project_id,
            # resource_id=key_id,
            # subresource_id=comment_id
        # )
        # return CommentModel(raw_comment)

    # def create_key_comments(self,
                            # project_id,
                            # key_id,
                            # params
                            # ):
        # u"""Creates one or more comments for the given key.

        # :param str project_id: ID of the project
        # :param key_id: ID of key to create comments for
        # :type key_id: int or str
        # :param params: Comment parameters
        # :type params: list or dict
        # :return: Collection of comments
        # """
        # raw_comments = self.get_endpoint(u"key_comments").create(
            # params=params,
            # wrapper_attr=u"comments",
            # parent_id=project_id,
            # resource_id=key_id
        # )
        # return CommentsCollection(raw_comments)

    # def delete_key_comment(self,
                           # project_id,
                           # key_id,
                           # comment_id
                           # ):
        # u"""Deletes a given key comment.

        # :param str project_id: ID of the project
        # :param key_id: ID of key to delete comment for.
        # :type key_id: int or str
        # :param comment_id: Comment to delete
        # :type comment_id: int or str
        # :return: Dictionary with project ID and "comment_deleted" set to True
        # """
        # response = self.get_endpoint(u"key_comments").delete(
            # parent_id=project_id,
            # resource_id=key_id,
            # subresource_id=comment_id
        # )
        # return response

    # def contributors(self,
                     # project_id,
                     # params = None
                     # ):
        # u"""Fetches all contributors for the given project.

        # :param str project_id: ID of the project to fetch contributors for.
        # :param dict params: (optional) Pagination params
        # :return: Collection of contributors
        # """
        # raw_contributors = self.get_endpoint(u"contributors"). \
            # all(parent_id=project_id, params=params)
        # return ContributorsCollection(raw_contributors)

    # def contributor(self,
                    # project_id,
                    # contributor_id):
        # u"""Fetches a single contributor.

        # :param str project_id: ID of the project
        # :param contributor_id: ID of the contributor to fetch
        # :type contributor_id: int or str
        # :return: Contributor model
        # """
        # raw_contributor = self.get_endpoint(u"contributors"). \
            # find(parent_id=project_id, resource_id=contributor_id)
        # return ContributorModel(raw_contributor)

    # def create_contributors(self,
                            # project_id,
                            # params
                            # ):
        # u"""Creates one or more contributors inside the project

        # :param str project_id: ID of the project
        # :param params: Contributors parameters
        # :type params: list or dict
        # :return: Contributors collection
        # """
        # raw_contributors = self.get_endpoint(u"contributors").create(
            # params=params,
            # wrapper_attr=u"contributors",
            # parent_id=project_id
        # )

        # return ContributorsCollection(raw_contributors)

    # def update_contributor(self,
                           # project_id,
                           # contributor_id,
                           # params):
        # u"""Updates a single contributor.

        # :param str project_id: ID of the project
        # :param contributor_id: ID of the contributor to update
        # :type contributor_id: int or str
        # :param dict params: Update parameters
        # :return: Contributor model
        # """
        # raw_contributor = self.get_endpoint(u"contributors").update(
            # params=params,
            # parent_id=project_id,
            # resource_id=contributor_id
        # )
        # return ContributorModel(raw_contributor)

    # def delete_contributor(self, project_id,
                           # contributor_id):
        # u"""Deletes a contributor.

        # :param str project_id: ID of the project
        # :param contributor_id: ID of the contributor to delete
        # :type contributor_id: int or str
        # :return: Dictionary with project ID and "contributor_deleted" set to True
        # :rtype dict:
        # """
        # response = self.get_endpoint(u"contributors"). \
            # delete(parent_id=project_id, resource_id=contributor_id)
        # return response

    # def files(self,
              # project_id,
              # params = None
              # ):
        # u"""Fetches all files for the given project.

        # :param str project_id: ID of the project to fetch files for.
        # :param dict params: (optional) Pagination params
        # :return: Collection of files
        # """
        # raw_files = self.get_endpoint(u"files"). \
            # all(parent_id=project_id, params=params)
        # return FilesCollection(raw_files)

    # def upload_file(self, project_id,
                    # params):
        # u"""Uploads a file to the given project.

        # :param str project_id: ID of the project to upload file to
        # :param dict params: Upload params
        # :return: Queued process model
        # """
        # raw_process = self.get_endpoint(u"files"). \
            # upload(params=params, parent_id=project_id)
        # return QueuedProcessModel(raw_process)

    # def download_files(self, project_id,
                       # params):
        # u"""Downloads files from the given project.

        # :param str project_id: ID of the project to download from
        # :param dict params: Download params
        # :return: Dictionary with project ID and a bundle URL
        # """
        # response = self.get_endpoint(u"files"). \
            # download(params=params, parent_id=project_id)
        # return response

    def keys(self,
             project_id,
             params = None
             ):
        u"""Fetches all keys for the given project.

        :param str project_id: ID of the project
        :param dict params: Request parameters
        :return: Collection of keys
        """
        raw_keys = self.get_endpoint(u"keys"). \
            all(parent_id=project_id, params=params)
        return KeysCollection(raw_keys)

    def create_keys(self,
                    project_id,
                    params
                    ):
        u"""Creates one or more keys inside the project

        :param str project_id: ID of the project
        :param params: Keys parameters
        :type params: list or dict
        :return: Keys collection
        """
        raw_keys = self.get_endpoint(u"keys"). \
            create(params=params, wrapper_attr=u"keys", parent_id=project_id)

        return KeysCollection(raw_keys)

    # def key(self,
            # project_id,
            # key_id,
            # params = None):
        # u"""Fetches a translation key.

        # :param str project_id: ID of the project
        # :param key_id: ID of the key to fetch
        # :param dict params: Request parameters
        # :return: Key model
        # """
        # raw_key = self.get_endpoint(u"keys"). \
            # find(params=params, parent_id=project_id, resource_id=key_id)
        # return KeyModel(raw_key)

    # def update_key(self,
                   # project_id,
                   # key_id,
                   # params = None):
        # u"""Updates a translation key.

        # :param str project_id: ID of the project
        # :param key_id: ID of the key to update
        # :param dict params: Request parameters
        # :return: Key model
        # """
        # raw_key = self.get_endpoint(u"keys"). \
            # update(params=params, parent_id=project_id, resource_id=key_id)
        # return KeyModel(raw_key)

    def update_keys(self,
                    project_id,
                    params):
        u"""Updates translation keys in bulk.

        :param str project_id: ID of the project
        :param dict params: Key parameters
        :return: Key collection
        """
        raw_keys = self.get_endpoint(u"keys"). \
            update(params=params, wrapper_attr=u"keys", parent_id=project_id)
        return KeysCollection(raw_keys)

    # def delete_key(self, project_id,
                   # key_id):
        # u"""Deletes a key.

        # :param str project_id: ID of the project
        # :param key_id: ID of the key to delete
        # :type key_id: int or str
        # :return: Dictionary with project ID and "key_removed" set to True
        # :rtype dict:
        # """
        # response = self.get_endpoint(u"keys"). \
            # delete(parent_id=project_id, resource_id=key_id)
        # return response

    # def delete_keys(self, project_id,
                    # key_ids):
        # u"""Deletes keys in bulk.

        # :param str project_id: ID of the project
        # :type key_id: int or str
        # :param list key_ids: List of the key identifiers to delete
        # :return: Dictionary with project ID and "keys_removed" set to True
        # :rtype dict:
        # """
        # response = self.get_endpoint(u"keys"). \
            # delete(params=key_ids, wrapper_attr=u"keys", parent_id=project_id)
        # return response

    # def system_languages(self,
                         # params = None
                         # ):
        # u"""Fetches all languages that Lokalise supports.

        # :param dict params: (optional) Pagination params
        # :return: Collection of languages
        # """
        # raw_languages = self.get_endpoint(
            # u"system_languages").all(params=params)
        # return LanguagesCollection(raw_languages)

    # def project_languages(self,
                          # project_id,
                          # params = None
                          # ):
        # u"""Fetches all languages for the given project.

        # :param str project_id: ID of the project
        # :param dict params: (optional) Pagination params
        # :return: Collection of languages
        # """
        # raw_languages = self.get_endpoint(u"languages"). \
            # all(parent_id=project_id, params=params)
        # return LanguagesCollection(raw_languages)

    # def create_languages(self,
                         # project_id,
                         # params):
        # u"""Create one or more languages for the given project.

        # :param str project_id: ID of the project
        # :param params: Language parameters
        # :type params: dict or list
        # :return: Collection of languages
        # """
        # raw_languages = self.get_endpoint(u"languages").create(
            # params=params,
            # wrapper_attr=u"languages",
            # parent_id=project_id
        # )
        # return LanguagesCollection(raw_languages)

    # def language(self,
                 # project_id,
                 # language_id):
        # u"""Fetches a project language.

        # :param str project_id: ID of the project
        # :param language_id: ID of the language to fetch
        # :return: Language model
        # """
        # raw_language = self.get_endpoint(u"languages"). \
            # find(parent_id=project_id, resource_id=language_id)
        # return LanguageModel(raw_language)

    # def update_language(self,
                        # project_id,
                        # language_id,
                        # params):
        # u"""Updates a project language.

        # :param str project_id: ID of the project
        # :param language_id: ID of the language to update
        # :param dict params: Update parameters
        # :return: Language model
        # """
        # raw_language = self.get_endpoint(u"languages").update(
            # params=params,
            # parent_id=project_id,
            # resource_id=language_id
        # )
        # return LanguageModel(raw_language)

    # def delete_language(self, project_id,
                        # language_id):
        # u"""Deletes a project language.

        # :param str project_id: ID of the project
        # :param language_id: ID of the language to delete
        # :return: Dictionary with project ID and "language_deleted" set to True
        # :rtype dict:
        # """
        # response = self.get_endpoint(u"languages"). \
            # delete(parent_id=project_id, resource_id=language_id)
        # return response

    # def orders(self,
               # team_id,
               # params = None
               # ):
        # u"""Fetches all orders for the given team.

        # :param team_id: ID of the team
        # :type team_id: int or str
        # :param dict params: (optional) Pagination params
        # :return: Collection of orders
        # """
        # raw_orders = self.get_endpoint(u"orders"). \
            # all(parent_id=team_id, params=params)
        # return OrdersCollection(raw_orders)

    # def order(self,
              # team_id,
              # order_id
              # ):
        # u"""Fetches an order for the given team.

        # :param team_id: ID of the team
        # :type team_id: int or str
        # :param str order_id: ID of the order
        # :return: Order model
        # """
        # raw_order = self.get_endpoint(u"orders"). \
            # find(parent_id=team_id, resource_id=order_id)
        # return OrderModel(raw_order)

    # def create_order(self,
                     # team_id,
                     # params
                     # ):
        # u"""Creates a new order inside the given team.

        # :param team_id: ID of the team
        # :type team_id: int or str
        # :param dict params: Order parameters
        # :return: Order model
        # """
        # raw_order = self.get_endpoint(u"orders"). \
            # create(parent_id=team_id, params=params)
        # return OrderModel(raw_order)

    # def payment_cards(self,
                      # params = None):
        # u"""Fetches all payment cards available to the currently authorized user
        # (identified by the API token).

        # :param dict params: (optional) Pagination params
        # :return: Collection of payment cards
        # """
        # raw_cards = self.get_endpoint(u"payment_cards").all(params=params)
        # return PaymentCardsCollection(raw_cards)

    # def payment_card(self,
                     # payment_card_id):
        # u"""Fetches a payment card by ID.

        # :param payment_card_id: ID of the payment card to fetch
        # :type payment_card_id: str or int
        # :return: Payment card model
        # """
        # raw_card = self.get_endpoint(u"payment_cards"). \
            # find(parent_id=payment_card_id)
        # return PaymentCardModel(raw_card)

    # def create_payment_card(self, params
                            # ):
        # u"""Creates a new payment card.

        # :param dict params: Payment card parameters
        # :return: Payment card model
        # """
        # raw_card = self.get_endpoint(u"payment_cards").create(params=params)
        # return PaymentCardModel(raw_card)

    # def delete_payment_card(self, payment_card_id):
        # u"""Deletes a payment card.

        # :param payment_card_id: ID of the payment card to delete
        # :type payment_card_id: int or str
        # :return: Dictionary with card ID and "card_deleted" set to True
        # :rtype dict:
        # """
        # resp = self.get_endpoint(u"payment_cards"). \
            # delete(parent_id=payment_card_id)
        # return resp

    # def projects(self, params = None):
        # u"""Fetches all projects available to the currently authorized user
        # (identified by the API token).

        # :param dict params: (optional) Pagination params
        # :return: Collection of projects
        # """
        # raw_projects = self.get_endpoint(u"projects").all(params=params)
        # return ProjectsCollection(raw_projects)

    # def project(self, project_id):
        # u"""Fetches a single project by ID.

        # :param str project_id: ID of the project to fetch
        # :return: Project model
        # """
        # raw_project = self.get_endpoint(u"projects"). \
            # find(parent_id=project_id)
        # return ProjectModel(raw_project)

    # def create_project(self, params):
        # u"""Creates a new project.

        # :param dict params: Project parameters
        # :return: Project model
        # """
        # raw_project = self.get_endpoint(u"projects").create(params=params)
        # return ProjectModel(raw_project)

    # def update_project(self, project_id,
                       # params):
        # u"""Updates a project.

        # :param str project_id: ID of the project to update
        # :param dict params: Project parameters
        # :return: Project model
        # """
        # raw_project = self.get_endpoint(u"projects").\
            # update(params=params, parent_id=project_id)
        # return ProjectModel(raw_project)

    # def empty_project(self, project_id):
        # u"""Empties a given project by removing all keys and translations.

        # :param str project_id: ID of the project to empty
        # :return: Dictionary with the project ID and "keys_deleted" set to True
        # :rtype dict:
        # """
        # return self.get_endpoint(u"projects").empty(parent_id=project_id)

    # def delete_project(self, project_id):
        # u"""Deletes a given project.

        # :param str project_id: ID of the project to delete
        # :return: Dictionary with project ID and "project_deleted" set to True
        # :rtype dict:
        # """
        # return self.get_endpoint(u"projects").delete(parent_id=project_id)

    # def queued_processes(self, project_id):
        # u"""Fetches all queued processes for the given project.

        # :param str project_id: ID of the project
        # :return: Collection of queued processes
        # """
        # raw_processes = self.get_endpoint(u"queued_processes"). \
            # all(parent_id=project_id)
        # return QueuedProcessesCollection(raw_processes)

    # def queued_process(self,
                       # project_id,
                       # queued_process_id):
        # u"""Fetches a queued process.

        # :param str project_id: ID of the project
        # :param queued_process_id: ID of the process to fetch
        # :type queued_process_id: int or str
        # :return: Queued process model
        # """
        # raw_process = self.get_endpoint(u"queued_processes"). \
            # find(parent_id=project_id, resource_id=queued_process_id)
        # return QueuedProcessModel(raw_process)

    # def snapshots(self, project_id,
                  # params = None):
        # u"""Fetches all snapshots for the given project.

        # :param str project_id: ID of the project
        # :param dict params: (optional) Pagination params
        # :return: Collection of snapshots
        # """
        # raw_snapshots = self.get_endpoint(u"snapshots"). \
            # all(params=params, parent_id=project_id)
        # return SnapshotsCollection(raw_snapshots)

    # def create_snapshot(self, project_id,
                        # params = None
                        # ):
        # u"""Creates a snapshot of the given project.

        # :param str project_id: ID of the project
        # :param dict params: (optional) Request params
        # :return: Snapshot model
        # """
        # raw_snapshot = self.get_endpoint(u"snapshots"). \
            # create(params=params, parent_id=project_id)
        # return SnapshotModel(raw_snapshot)

    # def restore_snapshot(self,
                         # project_id,
                         # snapshot_id):
        # u"""Restores a snapshot of the given project by producing a new project.

        # :param str project_id: ID of the project
        # :param queued_process_id: ID of the snapshot to restore
        # :type snapshot_id: int or str
        # :return: Snapshot model
        # """
        # new_project = self.get_endpoint(u"snapshots"). \
            # create(parent_id=project_id, resource_id=snapshot_id)
        # return ProjectModel(new_project)

    # def delete_snapshot(self, project_id,
                        # snapshot_id):
        # u"""Deletes a project snapshot.

        # :param str project_id: ID of the project
        # :param snapshot_id: ID of the snapshot to delete
        # :return: Dictionary with project ID and "snapshot_deleted" set to True
        # :rtype dict:
        # """
        # response = self.get_endpoint(u"snapshots"). \
            # delete(parent_id=project_id, resource_id=snapshot_id)
        # return response

    # def screenshots(self, project_id,
                    # params = None):
        # u"""Fetches all screenshots for the given project.

        # :param str project_id: ID of the project
        # :param dict params: (optional) Pagination params
        # :return: Collection of screenshots
        # """
        # raw_screenshots = self.get_endpoint(u"screenshots"). \
            # all(params=params, parent_id=project_id)
        # return ScreenshotsCollection(raw_screenshots)

    # def screenshot(self,
                   # project_id,
                   # screenshot_id):
        # u"""Fetches a screenshot.

        # :param str project_id: ID of the project
        # :param screenshot_id: ID of the screenshot to fetch
        # :type screenshot_id: int or str
        # :return: Screenshot model
        # """
        # screenshot = self.get_endpoint(u"screenshots"). \
            # find(parent_id=project_id, resource_id=screenshot_id)
        # return ScreenshotModel(screenshot)

    # def create_screenshots(self, project_id,
                           # params
                           # ):
        # u"""Creates one or more screenshots in the given project.

        # :param str project_id: ID of the project
        # :param params: Screenshots parameters
        # :type params: dict or list
        # :return: Collection of screenshots
        # """
        # raw_screenshots = self.get_endpoint(u"screenshots").create(
            # params=params,
            # wrapper_attr=u"screenshots",
            # parent_id=project_id
        # )
        # return ScreenshotsCollection(raw_screenshots)

    # def update_screenshot(self,
                          # project_id,
                          # screenshot_id,
                          # params = None
                          # ):
        # u"""Updates a screenshot.

        # :param str project_id: ID of the project
        # :param screenshot_id: ID of the screenshot to update
        # :type screenshot_id: int or str
        # :param dict params: Screenshots parameters
        # :return: Screenshot model
        # """
        # screenshot = self.get_endpoint(u"screenshots").update(
            # params=params,
            # parent_id=project_id,
            # resource_id=screenshot_id
        # )
        # return ScreenshotModel(screenshot)

    # def delete_screenshot(self,
                          # project_id,
                          # screenshot_id):
        # u"""Deletes a screenshot.

        # :param str project_id: ID of the project
        # :param screenshot_id: ID of the screenshot to delete
        # :type screenshot_id: int or str
        # :return: Dictionary with the project ID and "screenshot_deleted": True
        # """
        # response = self.get_endpoint(u"screenshots"). \
            # delete(parent_id=project_id, resource_id=screenshot_id)
        # return response

    # def tasks(self, project_id,
              # params = None):
        # u"""Fetches all tasks for the given project.

        # :param str project_id: ID of the project
        # :param dict params: (optional) Request parameters
        # :return: Collection of tasks
        # """
        # raw_tasks = self.get_endpoint(u"tasks"). \
            # all(params=params, parent_id=project_id)
        # return TasksCollection(raw_tasks)

    # def task(self,
             # project_id,
             # task_id):
        # u"""Fetches a task.

        # :param str project_id: ID of the project
        # :param task_id: ID of the task to fetch
        # :type task_id: int or str
        # :return: Task model
        # """
        # raw_task = self.get_endpoint(u"tasks"). \
            # find(parent_id=project_id, resource_id=task_id)
        # return TaskModel(raw_task)

    # def create_task(self, project_id,
                    # params):
        # u"""Creates a task in the given project.

        # :param str project_id: ID of the project
        # :param dict params: Task parameters
        # :return: Task model
        # """
        # raw_task = self.get_endpoint(u"tasks"). \
            # create(params=params, parent_id=project_id)
        # return TaskModel(raw_task)

    # def update_task(self,
                    # project_id,
                    # task_id,
                    # params = None
                    # ):
        # u"""Updates a task.

        # :param str project_id: ID of the project
        # :param task_id: ID of the task to update
        # :type task_id: int or str
        # :param dict params: Task parameters
        # :return: Task model
        # """
        # raw_task = self.get_endpoint(u"tasks"). \
            # update(params=params, parent_id=project_id, resource_id=task_id)
        # return TaskModel(raw_task)

    # def delete_task(self,
                    # project_id,
                    # task_id):
        # u"""Deletes a task.

        # :param str project_id: ID of the project
        # :param task_id: ID of the task to delete
        # :type task_id: int or str
        # :return: Dictionary with the project ID and "task_deleted": True
        # """
        # response = self.get_endpoint(u"tasks"). \
            # delete(parent_id=project_id, resource_id=task_id)
        # return response

    # def teams(self, params = None):
        # u"""Fetches all teams available to the currently authorized user
        # (identified by the API token).

        # :param dict params: (optional) Pagination params
        # :return: Collection of teams
        # """
        # raw_teams = self.get_endpoint(u"teams").all(params=params)
        # return TeamsCollection(raw_teams)

    # def team_users(self, team_id,
                   # params = None):
        # u"""Fetches all team users.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param dict params: (optional) Pagination parameters
        # :return: Collection of team users
        # """
        # raw_team_users = self.get_endpoint(u"team_users"). \
            # all(params=params, parent_id=team_id)
        # return TeamUsersCollection(raw_team_users)

    # def team_user(self, team_id,
                  # team_user_id):
        # u"""Fetches a team user.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_id: ID of the team user to fetch
        # :type team_user_id: str or int
        # :return: Team user model
        # """
        # raw_team_user = self.get_endpoint(u"team_users"). \
            # find(parent_id=team_id, resource_id=team_user_id)
        # return TeamUserModel(raw_team_user)

    # def update_team_user(self, team_id,
                         # team_user_id,
                         # params = None):
        # u"""Updates a team user.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_id: ID of the team user to update
        # :type team_user_id: str or int
        # :param dict params: (optional) Team user parameters
        # :return: Team user model
        # """
        # raw_team_user = self.get_endpoint(u"team_users"). \
            # update(params=params, parent_id=team_id, resource_id=team_user_id)
        # return TeamUserModel(raw_team_user)

    # def delete_team_user(self, team_id,
                         # team_user_id):
        # u"""Deletes a team user.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_id: ID of the team user to delete
        # :type team_user_id: str or int
        # :return: Dict with the team ID and `team_user_deleted` set to True
        # """
        # response = self.get_endpoint(u"team_users"). \
            # delete(parent_id=team_id, resource_id=team_user_id)
        # return response

    # def team_user_groups(self, team_id,
                         # params = None
                         # ):
        # u"""Fetches all team user groups.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param dict params: (optional) Pagination parameters
        # :return: Collection of team user groups
        # """
        # raw_groups = self.get_endpoint(u"team_user_groups"). \
            # all(params=params, parent_id=team_id)
        # return TeamUserGroupsCollection(raw_groups)

    # def team_user_group(self, team_id,
                        # team_user_group_id
                        # ):
        # u"""Fetches a team user group.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_group_id: ID of the team user group to fetch
        # :type team_user_group_id: str or int
        # :return: Team user group model
        # """
        # raw_group = self.get_endpoint(u"team_user_groups"). \
            # find(parent_id=team_id, resource_id=team_user_group_id)
        # return TeamUserGroupModel(raw_group)

    # def create_team_user_group(self, team_id,
                               # params
                               # ):
        # u"""Fetches a team user group.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param dict params: Team user group parameters
        # :return: Team user group model
        # """
        # raw_group = self.get_endpoint(u"team_user_groups"). \
            # create(params=params, parent_id=team_id)
        # return TeamUserGroupModel(raw_group)

    # def update_team_user_group(self, team_id,
                               # team_user_group_id,
                               # params
                               # ):
        # u"""Updates a team user group.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_group_id: ID of the team user group to update
        # :type team_user_group_id: str or int
        # :param dict params: Team user group parameters
        # :return: Team user group model
        # """
        # raw_group = self.get_endpoint(u"team_user_groups").update(
            # params=params,
            # parent_id=team_id,
            # resource_id=team_user_group_id
        # )
        # return TeamUserGroupModel(raw_group)

    # def delete_team_user_group(self, team_id,
                               # team_user_group_id
                               # ):
        # u"""Deletes a team user group.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_group_id: ID of the team user group to delete
        # :type team_user_group_id: str or int
        # :return: Dict with team ID and `group_deleted` set to True
        # """
        # response = self.get_endpoint(u"team_user_groups"). \
            # delete(parent_id=team_id, resource_id=team_user_group_id)
        # return response

    # def add_projects_to_group(self, team_id,
                              # team_user_group_id,
                              # params
                              # ):
        # u"""Adds projects to a team user group.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_group_id: ID of the team user group to add projects to
        # :type team_user_group_id: str or int
        # :param params: Project IDs to add to the group
        # :type params: list or str
        # :return: Team user group model
        # """
        # raw_group = self.get_endpoint(u"team_user_groups").add_projects(
            # params=params,
            # parent_id=team_id,
            # resource_id=team_user_group_id
        # )
        # return TeamUserGroupModel(raw_group)

    # def remove_projects_from_group(self, team_id,
                                   # team_user_group_id,
                                   # params
                                   # ):
        # u"""Removes projects from a team user group.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_group_id: ID of the team user group to remove projects from
        # :type team_user_group_id: str or int
        # :param params: Project IDs to remove from the group
        # :type params: list or str
        # :return: Team user group model
        # """
        # raw_group = self.get_endpoint(u"team_user_groups").remove_projects(
            # params=params,
            # parent_id=team_id,
            # resource_id=team_user_group_id
        # )
        # return TeamUserGroupModel(raw_group)

    # def add_members_to_group(self, team_id,
                             # team_user_group_id,
                             # params
                             # ):
        # u"""Adds members to a team user group.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_group_id: ID of the team user group to add members to
        # :type team_user_group_id: str or int
        # :param params: User IDs to add to the group
        # :type params: list or str
        # :return: Team user group model
        # """
        # raw_group = self.get_endpoint(u"team_user_groups").add_members(
            # params=params,
            # parent_id=team_id,
            # resource_id=team_user_group_id
        # )
        # return TeamUserGroupModel(raw_group)

    # def remove_members_from_group(self, team_id,
                                  # team_user_group_id,
                                  # params
                                  # ):
        # u"""Removes members from a team user group.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param team_user_group_id: ID of the team user group to remove members from
        # :type team_user_group_id: str or int
        # :param params: User IDs to remove from the group
        # :type params: list or str
        # :return: Team user group model
        # """
        # raw_group = self.get_endpoint(u"team_user_groups").remove_members(
            # params=params,
            # parent_id=team_id,
            # resource_id=team_user_group_id
        # )
        # return TeamUserGroupModel(raw_group)

    # def translations(self, project_id,
                     # params = None):
        # u"""Fetches all translations for the given project.

        # :param str project_id: ID of the project
        # :param dict params: (optional) Request parameters
        # :return: Collection of translations
        # """
        # raw_translations = self.get_endpoint(u"translations"). \
            # all(params=params, parent_id=project_id)
        # return TranslationsCollection(raw_translations)

    # def translation(self,
                    # project_id,
                    # translation_id,
                    # params = None):
        # u"""Fetches a translation.

        # :param str project_id: ID of the project
        # :param translation_id: ID of the translation to fetch
        # :type translation_id: int or str
        # :param dict params: (optional) Request parameters
        # :return: Task model
        # """
        # raw_translation = self.get_endpoint(u"translations"). \
            # find(params, parent_id=project_id, resource_id=translation_id)
        # return TranslationModel(raw_translation)

    # def update_translation(self,
                           # project_id,
                           # translation_id,
                           # params):
        # u"""Updates a translation.

        # :param str project_id: ID of the project
        # :param translation_id: ID of the translation to update
        # :type translation_id: int or str
        # :param dict params: Translation parameters
        # :return: Task model
        # """
        # raw_translation = self.get_endpoint(u"translations").update(
            # params=params,
            # parent_id=project_id,
            # resource_id=translation_id
        # )
        # return TranslationModel(raw_translation)

    # def translation_providers(self, team_id,
                              # params = None
                              # ):
        # u"""Fetches all translation providers.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param dict params: (optional) Pagination parameters
        # :return: Collection of translation providers
        # """
        # raw_providers = self.get_endpoint(u"translation_providers"). \
            # all(params=params, parent_id=team_id)
        # return TranslationProvidersCollection(raw_providers)

    # def translation_provider(self, team_id,
                             # translation_provider_id
                             # ):
        # u"""Fetches a translation provider.

        # :param team_id: ID of the team
        # :type team_id: str or int
        # :param translation_provider_id: ID of the translation provider to fetch
        # :type translation_provider_id: str or int
        # :return: Translation provider model
        # """
        # raw_provider = self.get_endpoint(u"translation_providers"). \
            # find(parent_id=team_id, resource_id=translation_provider_id)
        # return TranslationProviderModel(raw_provider)

    # def translation_statuses(self, project_id,
                             # params = None
                             # ):
        # u"""Fetches all translation statuses.

        # :param str project_id: ID of the project
        # :param dict params: (optional) Pagination parameters
        # :return: Collection of translation statuses
        # """
        # raw_statuses = self.get_endpoint(u"translation_statuses"). \
            # all(params=params, parent_id=project_id)
        # return TranslationStatusesCollection(raw_statuses)

    # def translation_status(self, project_id,
                           # translation_status_id,
                           # ):
        # u"""Fetches a translation status.

        # :param str project_id: ID of the project
        # :param translation_status_id: ID of the status to fetch
        # :type translation_status_id: int or str
        # :return: Translation status model
        # """
        # raw_status = self.get_endpoint(u"translation_statuses"). \
            # find(parent_id=project_id, resource_id=translation_status_id)
        # return TranslationStatusModel(raw_status)

    # def create_translation_status(self, project_id,
                                  # params
                                  # ):
        # u"""Creates a translation status.

        # :param str project_id: ID of the project
        # :param dict params: Translation status parameters
        # :return: Translation status model
        # """
        # raw_status = self.get_endpoint(u"translation_statuses"). \
            # create(params=params, parent_id=project_id)
        # return TranslationStatusModel(raw_status)

    # def update_translation_status(self, project_id,
                                  # translation_status_id,
                                  # params = None
                                  # ):
        # u"""Updates a translation status.

        # :param str project_id: ID of the project
        # :param translation_status_id: ID of the status to update
        # :type translation_status_id: int or str
        # :param dict params: Translation status parameters
        # :return: Translation status model
        # """
        # raw_status = self.get_endpoint(u"translation_statuses").update(
            # params=params,
            # parent_id=project_id,
            # resource_id=translation_status_id
        # )
        # return TranslationStatusModel(raw_status)

    # def delete_translation_status(self, project_id,
                                  # translation_status_id,
                                  # ):
        # u"""Deletes a translation status.

        # :param str project_id: ID of the project
        # :param translation_status_id: ID of the status to delete
        # :type translation_status_id: int or str
        # :return: Dict with project ID and `custom_translation_status_deleted`: True
        # """
        # response = self.get_endpoint(u"translation_statuses"). \
            # delete(parent_id=project_id, resource_id=translation_status_id)
        # return response

    # def translation_statuses_colors(self, project_id):
        # u"""Fetches available RGB colors that can be assigned to
        # translation statuses.

        # :param str project_id: ID of the project
        # :return: List with the RGB color codes
        # """
        # response = self.get_endpoint(u"translation_statuses"). \
            # colors(parent_id=project_id)
        # return response[u"colors"]

    # def webhooks(self, project_id,
                 # params = None
                 # ):
        # u"""Lists all webhooks set for a project.

        # :param str project_id: ID of the project
        # :param dict params: Pagination parameters
        # :return: Webhook collection
        # """
        # raw_webhooks = self.get_endpoint(u"webhooks"). \
            # all(params=params, parent_id=project_id)
        # return WebhooksCollection(raw_webhooks)

    # def webhook(self, project_id, webhook_id):
        # u"""Fetches a webhook.

        # :param str project_id: ID of the project
        # :param str webhook_id: ID of the webhook to fetch
        # :return: Webhook model
        # """
        # raw_webhook = self.get_endpoint(u"webhooks"). \
            # find(parent_id=project_id, resource_id=webhook_id)
        # return WebhookModel(raw_webhook)

    # def create_webhook(self, project_id,
                       # params
                       # ):
        # u"""Creates a webhook.

        # :param str project_id: ID of the project
        # :param dict params: Webhook parameters
        # :return: Webhook model
        # """
        # raw_webhook = self.get_endpoint(u"webhooks"). \
            # create(params=params, parent_id=project_id)
        # return WebhookModel(raw_webhook)

    # def update_webhook(self, project_id, webhook_id,
                       # params = None):
        # u"""Updates a webhook.

        # :param str project_id: ID of the project
        # :param str webhook_id: ID of the webhook to update
        # :param dict params: Webhook parameters
        # :return: Webhook model
        # """
        # raw_webhook = self.get_endpoint(u"webhooks"). \
            # update(params=params, parent_id=project_id, resource_id=webhook_id)
        # return WebhookModel(raw_webhook)

    # def delete_webhook(self, project_id, webhook_id):
        # u"""Deletes a webhook.

        # :param str project_id: ID of the project
        # :param str webhook_id: ID of the webhook to delete
        # :return: Dict with project ID and `webhook_deleted` set to True
        # """
        # response = self.get_endpoint(u"webhooks"). \
            # delete(parent_id=project_id, resource_id=webhook_id)
        # return response

    # def regenerate_webhook_secret(self, project_id,
                                  # webhook_id):
        # u"""Regenerates a secret key for the webhook.

        # :param str project_id: ID of the project
        # :param str webhook_id: ID of the webhook to regenerate secret for
        # :return: Dict with project ID and `secret` with the new secret's value
        # """
        # response = self.get_endpoint(u"webhooks"). \
            # regenerate_secret(parent_id=project_id, resource_id=webhook_id)
        # return response
    # # === End of endpoint methods ===

    # === Endpoint helpers
    def get_endpoint(self, name):
        u"""Lazily loads an endpoint with a given name and stores it
        under a specific instance attribute. For example, if the `name`
        is "projects", then it will load .endpoints.projects_endpoint module
        and then set attribute like this:
            self.__projects_endpoint = ProjectsEndpoint(self)

        :param str name: Endpoint name to load
        """
        endpoint_name = name + u"_endpoint"
        camelized_name = snake_to_camel(endpoint_name)
        # Dynamically load the necessary endpoint module
        module = importlib.import_module(
            u".endpoints.{endpoint_name}".format(endpoint_name=endpoint_name), package=u'lokalise')
        # Find endpoint class in the module
        endpoint_klass = getattr(module, camelized_name)
        return self.__fetch_attr(u"__{endpoint_name}".format(endpoint_name=endpoint_name),
                                 lambda: endpoint_klass(self))

    def __fetch_attr(self, attr_name, populator):
        u"""Searches for the given attribute. Uses populator
        to set the attribute if it cannot be found. Used to lazy-load
        endpoints.
        """
        if not hasattr(self, attr_name):
            setattr(self, attr_name, populator())

        return getattr(self, attr_name)

    # def __clear_endpoint_attrs(self):
        # u"""Clears all lazily-loaded endpoint attributes
        # """
        # endpoint_attrs = [a for a in vars(self) if a.endswith(u'_endpoint')]
        # for attr in endpoint_attrs:
            # setattr(self, attr, None)
