# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Optional, Union

from amundsen_common.models.dashboard import DashboardSummary
from amundsen_common.models.lineage import Lineage
from amundsen_common.models.popular_table import PopularTable
from amundsen_common.models.table import Table
from amundsen_common.models.user import User

from metadata_service.entity.dashboard_detail import \
    DashboardDetail as DashboardDetailEntity
from metadata_service.entity.description import Description
from metadata_service.entity.resource_type import ResourceType
from metadata_service.util import UserResourceRel


class BaseProxy(metaclass=ABCMeta):
    """
    Base Proxy, which behaves like an interface for all
    the proxy clients available in the amundsen metadata service
    """

    @abstractmethod
    def get_user(self, *, id: str) -> Union[User, None]:
        pass

    @abstractmethod
    def get_users(self) -> List[User]:
        pass

    @abstractmethod
    def get_table(self, *, table_uri: str) -> Table:
        pass

    @abstractmethod
    def get_table_columns(self, *, table_uri: str) -> Table:
        pass

    @abstractmethod
    def delete_owner(self, *, table_uri: str, owner: str) -> None:
        pass

    @abstractmethod
    def add_owner(self, *, table_uri: str, owner: str) -> None:
        pass

    @abstractmethod
    def get_table_description(self, *,
                              table_uri: str) -> Union[str, None]:
        pass

    @abstractmethod
    def put_table_description(self, *,
                              table_uri: str,
                              description: str) -> None:
        pass

    @abstractmethod
    def add_tag(self, *, id: str, tag: str, tag_type: str, resource_type: ResourceType) -> None:
        pass

    @abstractmethod
    def add_badge(self, *, id: str, badge_name: str, category: str = '',
                  resource_type: ResourceType) -> None:
        pass

    @abstractmethod
    def delete_tag(self, *, id: str, tag: str, tag_type: str, resource_type: ResourceType) -> None:
        pass

    @abstractmethod
    def delete_badge(self, *, id: str, badge_name: str, category: str,
                     resource_type: ResourceType) -> None:
        pass

    @abstractmethod
    def put_column_description(self, *,
                               table_uri: str,
                               column_name: str,
                               description: str) -> None:
        pass

    @abstractmethod
    def get_column_description(self, *,
                               table_uri: str,
                               column_name: str) -> Union[str, None]:
        pass

    @abstractmethod
    def get_popular_tables(self, *,
                           num_entries: int,
                           user_id: Optional[str] = None) -> List[PopularTable]:
        pass

    @abstractmethod
    def get_latest_updated_ts(self) -> int:
        pass

    @abstractmethod
    def get_tags(self) -> List:
        pass

    @abstractmethod
    def get_badges(self) -> List:
        pass

    @abstractmethod
    def get_dashboard_by_user_relation(self, *, user_email: str, relation_type: UserResourceRel) \
            -> Dict[str, List[DashboardSummary]]:
        pass

    @abstractmethod
    def get_table_by_user_relation(self, *, user_email: str,
                                   relation_type: UserResourceRel) -> Dict[str, Any]:
        pass

    @abstractmethod
    def get_frequently_used_tables(self, *, user_email: str) -> Dict[str, Any]:
        pass

    @abstractmethod
    def add_resource_relation_by_user(self, *,
                                      id: str,
                                      user_id: str,
                                      relation_type: UserResourceRel,
                                      resource_type: ResourceType) -> None:
        pass

    @abstractmethod
    def delete_resource_relation_by_user(self, *,
                                         id: str,
                                         user_id: str,
                                         relation_type: UserResourceRel,
                                         resource_type: ResourceType) -> None:
        pass

    @abstractmethod
    def get_dashboard(self,
                      dashboard_uri: str,
                      ) -> DashboardDetailEntity:
        pass

    @abstractmethod
    def get_dashboard_description(self, *,
                                  id: str) -> Description:
        pass

    @abstractmethod
    def put_dashboard_description(self, *,
                                  id: str,
                                  description: str) -> None:
        pass

    @abstractmethod
    def get_resources_using_table(self, *,
                                  id: str,
                                  resource_type: ResourceType) -> Dict[str, List[DashboardSummary]]:
        pass

    @abstractmethod
    def get_lineage(self, *,
                    id: str, resource_type: ResourceType, direction: str, depth: int) -> Lineage:
        """
        Method should be implemented to obtain lineage from whatever source is preferred internally
        :param direction: if the request is for a list of upstream/downstream nodes or both
        :param depth: the level of lineage requested (ex: 1 would mean only nodes directly connected
        to the current id in whatever direction is specified)
        """
        pass
