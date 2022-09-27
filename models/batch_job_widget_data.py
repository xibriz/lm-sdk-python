# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.batch_job_execution_item import BatchJobExecutionItem  # noqa: F401,E501
from logicmonitor_sdk.models.widget_data import WidgetData  # noqa: F401,E501


class BatchJobWidgetData(WidgetData):
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
        'type': 'str',
        'title': 'str',
        'items': 'list[BatchJobExecutionItem]'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'items': 'items'
    }

    def __init__(self, type=None, title=None, items=None):  # noqa: E501
        """BatchJobWidgetData - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._title = None
        self._items = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if items is not None:
            self.items = items

    @property
    def type(self):
        """Gets the type of this BatchJobWidgetData.  # noqa: E501

        the widget data type. noc|alert|batchjob|gmap|netflow|netflowGroup|bigNumber|serviceNOC|gauge|pieChart|table|deviceNOC|deviceSLA|serviceSLA|dynamicTable|graph|savedMap  # noqa: E501

        :return: The type of this BatchJobWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchJobWidgetData.

        the widget data type. noc|alert|batchjob|gmap|netflow|netflowGroup|bigNumber|serviceNOC|gauge|pieChart|table|deviceNOC|deviceSLA|serviceSLA|dynamicTable|graph|savedMap  # noqa: E501

        :param type: The type of this BatchJobWidgetData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this BatchJobWidgetData.  # noqa: E501

        the widget title  # noqa: E501

        :return: The title of this BatchJobWidgetData.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BatchJobWidgetData.

        the widget title  # noqa: E501

        :param title: The title of this BatchJobWidgetData.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def items(self):
        """Gets the items of this BatchJobWidgetData.  # noqa: E501


        :return: The items of this BatchJobWidgetData.  # noqa: E501
        :rtype: list[BatchJobExecutionItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this BatchJobWidgetData.


        :param items: The items of this BatchJobWidgetData.  # noqa: E501
        :type: list[BatchJobExecutionItem]
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
        if issubclass(BatchJobWidgetData, dict):
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
        if not isinstance(other, BatchJobWidgetData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
