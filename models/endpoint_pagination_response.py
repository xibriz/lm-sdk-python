# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.netflow_endpoint import NetflowEndpoint  # noqa: F401,E501


class EndpointPaginationResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total': 'int',
        'search_id': 'str',
        'items': 'list[NetflowEndpoint]'
    }

    attribute_map = {
        'total': 'total',
        'search_id': 'searchId',
        'items': 'items'
    }

    def __init__(self, total=None, search_id=None, items=None):  # noqa: E501
        """EndpointPaginationResponse - a model defined in Swagger"""  # noqa: E501

        self._total = None
        self._search_id = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if search_id is not None:
            self.search_id = search_id
        if items is not None:
            self.items = items

    @property
    def total(self):
        """Gets the total of this EndpointPaginationResponse.  # noqa: E501


        :return: The total of this EndpointPaginationResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this EndpointPaginationResponse.


        :param total: The total of this EndpointPaginationResponse.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def search_id(self):
        """Gets the search_id of this EndpointPaginationResponse.  # noqa: E501


        :return: The search_id of this EndpointPaginationResponse.  # noqa: E501
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """Sets the search_id of this EndpointPaginationResponse.


        :param search_id: The search_id of this EndpointPaginationResponse.  # noqa: E501
        :type: str
        """

        self._search_id = search_id

    @property
    def items(self):
        """Gets the items of this EndpointPaginationResponse.  # noqa: E501


        :return: The items of this EndpointPaginationResponse.  # noqa: E501
        :rtype: list[NetflowEndpoint]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this EndpointPaginationResponse.


        :param items: The items of this EndpointPaginationResponse.  # noqa: E501
        :type: list[NetflowEndpoint]
        """

        self._items = items

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EndpointPaginationResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EndpointPaginationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
