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

from logicmonitor_sdk.models.big_number_data_point import BigNumberDataPoint  # noqa: F401,E501
from logicmonitor_sdk.models.big_number_item import BigNumberItem  # noqa: F401,E501
from logicmonitor_sdk.models.counter import Counter  # noqa: F401,E501
from logicmonitor_sdk.models.virtual_data_point import VirtualDataPoint  # noqa: F401,E501


class BigNumberInfo(object):
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
        'virtual_data_points': 'list[VirtualDataPoint]',
        'counters': 'list[Counter]',
        'data_points': 'list[BigNumberDataPoint]',
        'big_number_items': 'list[BigNumberItem]'
    }

    attribute_map = {
        'virtual_data_points': 'virtualDataPoints',
        'counters': 'counters',
        'data_points': 'dataPoints',
        'big_number_items': 'bigNumberItems'
    }

    def __init__(self, virtual_data_points=None, counters=None, data_points=None, big_number_items=None):  # noqa: E501
        """BigNumberInfo - a model defined in Swagger"""  # noqa: E501

        self._virtual_data_points = None
        self._counters = None
        self._data_points = None
        self._big_number_items = None
        self.discriminator = None

        if virtual_data_points is not None:
            self.virtual_data_points = virtual_data_points
        if counters is not None:
            self.counters = counters
        self.data_points = data_points
        self.big_number_items = big_number_items

    @property
    def virtual_data_points(self):
        """Gets the virtual_data_points of this BigNumberInfo.  # noqa: E501

        The virtual datapoints included in the widget. Note that a virtual datapoint must be referenced in the bigNumberItems object in order to be displayed  # noqa: E501

        :return: The virtual_data_points of this BigNumberInfo.  # noqa: E501
        :rtype: list[VirtualDataPoint]
        """
        return self._virtual_data_points

    @virtual_data_points.setter
    def virtual_data_points(self, virtual_data_points):
        """Sets the virtual_data_points of this BigNumberInfo.

        The virtual datapoints included in the widget. Note that a virtual datapoint must be referenced in the bigNumberItems object in order to be displayed  # noqa: E501

        :param virtual_data_points: The virtual_data_points of this BigNumberInfo.  # noqa: E501
        :type: list[VirtualDataPoint]
        """

        self._virtual_data_points = virtual_data_points

    @property
    def counters(self):
        """Gets the counters of this BigNumberInfo.  # noqa: E501

        The counter is used for saving applyTo expression, it's mainly used for count device  # noqa: E501

        :return: The counters of this BigNumberInfo.  # noqa: E501
        :rtype: list[Counter]
        """
        return self._counters

    @counters.setter
    def counters(self, counters):
        """Sets the counters of this BigNumberInfo.

        The counter is used for saving applyTo expression, it's mainly used for count device  # noqa: E501

        :param counters: The counters of this BigNumberInfo.  # noqa: E501
        :type: list[Counter]
        """

        self._counters = counters

    @property
    def data_points(self):
        """Gets the data_points of this BigNumberInfo.  # noqa: E501

        The datapoints included in the widget. Note that a datapoint must be referenced in the bigNumberItems object in order to be displayed  # noqa: E501

        :return: The data_points of this BigNumberInfo.  # noqa: E501
        :rtype: list[BigNumberDataPoint]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this BigNumberInfo.

        The datapoints included in the widget. Note that a datapoint must be referenced in the bigNumberItems object in order to be displayed  # noqa: E501

        :param data_points: The data_points of this BigNumberInfo.  # noqa: E501
        :type: list[BigNumberDataPoint]
        """
        if data_points is None:
            raise ValueError("Invalid value for `data_points`, must not be `None`")  # noqa: E501

        self._data_points = data_points

    @property
    def big_number_items(self):
        """Gets the big_number_items of this BigNumberInfo.  # noqa: E501

        The datapoints and virtual datapoints whose values should be displayed in the big number widget  # noqa: E501

        :return: The big_number_items of this BigNumberInfo.  # noqa: E501
        :rtype: list[BigNumberItem]
        """
        return self._big_number_items

    @big_number_items.setter
    def big_number_items(self, big_number_items):
        """Sets the big_number_items of this BigNumberInfo.

        The datapoints and virtual datapoints whose values should be displayed in the big number widget  # noqa: E501

        :param big_number_items: The big_number_items of this BigNumberInfo.  # noqa: E501
        :type: list[BigNumberItem]
        """
        if big_number_items is None:
            raise ValueError("Invalid value for `big_number_items`, must not be `None`")  # noqa: E501

        self._big_number_items = big_number_items

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
        if issubclass(BigNumberInfo, dict):
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
        if not isinstance(other, BigNumberInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
