# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DeviceDataSourceInstanceData(object):
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
        'data_source_name': 'str',
        'next_page_params': 'str',
        'time': 'list[int]',
        'values': 'list[list[object]]'
    }

    attribute_map = {
        'data_source_name': 'dataSourceName',
        'next_page_params': 'nextPageParams',
        'time': 'time',
        'values': 'values'
    }

    def __init__(self, data_source_name=None, next_page_params=None, time=None, values=None):  # noqa: E501
        """DeviceDataSourceInstanceData - a model defined in Swagger"""  # noqa: E501

        self._data_source_name = None
        self._next_page_params = None
        self._time = None
        self._values = None
        self.discriminator = None

        if data_source_name is not None:
            self.data_source_name = data_source_name
        if next_page_params is not None:
            self.next_page_params = next_page_params
        if time is not None:
            self.time = time
        if values is not None:
            self.values = values

    @property
    def data_source_name(self):
        """Gets the data_source_name of this DeviceDataSourceInstanceData.  # noqa: E501


        :return: The data_source_name of this DeviceDataSourceInstanceData.  # noqa: E501
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        """Sets the data_source_name of this DeviceDataSourceInstanceData.


        :param data_source_name: The data_source_name of this DeviceDataSourceInstanceData.  # noqa: E501
        :type: str
        """

        self._data_source_name = data_source_name

    @property
    def next_page_params(self):
        """Gets the next_page_params of this DeviceDataSourceInstanceData.  # noqa: E501


        :return: The next_page_params of this DeviceDataSourceInstanceData.  # noqa: E501
        :rtype: str
        """
        return self._next_page_params

    @next_page_params.setter
    def next_page_params(self, next_page_params):
        """Sets the next_page_params of this DeviceDataSourceInstanceData.


        :param next_page_params: The next_page_params of this DeviceDataSourceInstanceData.  # noqa: E501
        :type: str
        """

        self._next_page_params = next_page_params

    @property
    def time(self):
        """Gets the time of this DeviceDataSourceInstanceData.  # noqa: E501


        :return: The time of this DeviceDataSourceInstanceData.  # noqa: E501
        :rtype: list[int]
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this DeviceDataSourceInstanceData.


        :param time: The time of this DeviceDataSourceInstanceData.  # noqa: E501
        :type: list[int]
        """

        self._time = time

    @property
    def values(self):
        """Gets the values of this DeviceDataSourceInstanceData.  # noqa: E501


        :return: The values of this DeviceDataSourceInstanceData.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this DeviceDataSourceInstanceData.


        :param values: The values of this DeviceDataSourceInstanceData.  # noqa: E501
        :type: list[list[object]]
        """

        self._values = values

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
        if issubclass(DeviceDataSourceInstanceData, dict):
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
        if not isinstance(other, DeviceDataSourceInstanceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
