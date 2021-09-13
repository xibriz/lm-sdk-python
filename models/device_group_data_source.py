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


class DeviceGroupDataSource(object):
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
        'stop_monitoring': 'bool',
        'data_source_id': 'int',
        'data_source_group_name': 'str',
        'device_group_id': 'int',
        'data_source_display_name': 'str',
        'disable_alerting': 'bool',
        'data_source_name': 'str',
        'data_source_type': 'str'
    }

    attribute_map = {
        'stop_monitoring': 'stopMonitoring',
        'data_source_id': 'dataSourceId',
        'data_source_group_name': 'dataSourceGroupName',
        'device_group_id': 'deviceGroupId',
        'data_source_display_name': 'dataSourceDisplayName',
        'disable_alerting': 'disableAlerting',
        'data_source_name': 'dataSourceName',
        'data_source_type': 'dataSourceType'
    }

    def __init__(self, stop_monitoring=None, data_source_id=None, data_source_group_name=None, device_group_id=None, data_source_display_name=None, disable_alerting=None, data_source_name=None, data_source_type=None):  # noqa: E501
        """DeviceGroupDataSource - a model defined in Swagger"""  # noqa: E501

        self._stop_monitoring = None
        self._data_source_id = None
        self._data_source_group_name = None
        self._device_group_id = None
        self._data_source_display_name = None
        self._disable_alerting = None
        self._data_source_name = None
        self._data_source_type = None
        self.discriminator = None

        if stop_monitoring is not None:
            self.stop_monitoring = stop_monitoring
        if data_source_id is not None:
            self.data_source_id = data_source_id
        if data_source_group_name is not None:
            self.data_source_group_name = data_source_group_name
        if device_group_id is not None:
            self.device_group_id = device_group_id
        if data_source_display_name is not None:
            self.data_source_display_name = data_source_display_name
        if disable_alerting is not None:
            self.disable_alerting = disable_alerting
        if data_source_name is not None:
            self.data_source_name = data_source_name
        if data_source_type is not None:
            self.data_source_type = data_source_type

    @property
    def stop_monitoring(self):
        """Gets the stop_monitoring of this DeviceGroupDataSource.  # noqa: E501

        Boolean flag for enabling/disabling monitoring of DataSource  # noqa: E501

        :return: The stop_monitoring of this DeviceGroupDataSource.  # noqa: E501
        :rtype: bool
        """
        return self._stop_monitoring

    @stop_monitoring.setter
    def stop_monitoring(self, stop_monitoring):
        """Sets the stop_monitoring of this DeviceGroupDataSource.

        Boolean flag for enabling/disabling monitoring of DataSource  # noqa: E501

        :param stop_monitoring: The stop_monitoring of this DeviceGroupDataSource.  # noqa: E501
        :type: bool
        """

        self._stop_monitoring = stop_monitoring

    @property
    def data_source_id(self):
        """Gets the data_source_id of this DeviceGroupDataSource.  # noqa: E501

        The ID of the DataSource  # noqa: E501

        :return: The data_source_id of this DeviceGroupDataSource.  # noqa: E501
        :rtype: int
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this DeviceGroupDataSource.

        The ID of the DataSource  # noqa: E501

        :param data_source_id: The data_source_id of this DeviceGroupDataSource.  # noqa: E501
        :type: int
        """

        self._data_source_id = data_source_id

    @property
    def data_source_group_name(self):
        """Gets the data_source_group_name of this DeviceGroupDataSource.  # noqa: E501

        The DataSource Group name  # noqa: E501

        :return: The data_source_group_name of this DeviceGroupDataSource.  # noqa: E501
        :rtype: str
        """
        return self._data_source_group_name

    @data_source_group_name.setter
    def data_source_group_name(self, data_source_group_name):
        """Sets the data_source_group_name of this DeviceGroupDataSource.

        The DataSource Group name  # noqa: E501

        :param data_source_group_name: The data_source_group_name of this DeviceGroupDataSource.  # noqa: E501
        :type: str
        """

        self._data_source_group_name = data_source_group_name

    @property
    def device_group_id(self):
        """Gets the device_group_id of this DeviceGroupDataSource.  # noqa: E501

        The ID of the Device Group for the DataSource  # noqa: E501

        :return: The device_group_id of this DeviceGroupDataSource.  # noqa: E501
        :rtype: int
        """
        return self._device_group_id

    @device_group_id.setter
    def device_group_id(self, device_group_id):
        """Sets the device_group_id of this DeviceGroupDataSource.

        The ID of the Device Group for the DataSource  # noqa: E501

        :param device_group_id: The device_group_id of this DeviceGroupDataSource.  # noqa: E501
        :type: int
        """

        self._device_group_id = device_group_id

    @property
    def data_source_display_name(self):
        """Gets the data_source_display_name of this DeviceGroupDataSource.  # noqa: E501

        The Display Name of the DataSource  # noqa: E501

        :return: The data_source_display_name of this DeviceGroupDataSource.  # noqa: E501
        :rtype: str
        """
        return self._data_source_display_name

    @data_source_display_name.setter
    def data_source_display_name(self, data_source_display_name):
        """Sets the data_source_display_name of this DeviceGroupDataSource.

        The Display Name of the DataSource  # noqa: E501

        :param data_source_display_name: The data_source_display_name of this DeviceGroupDataSource.  # noqa: E501
        :type: str
        """

        self._data_source_display_name = data_source_display_name

    @property
    def disable_alerting(self):
        """Gets the disable_alerting of this DeviceGroupDataSource.  # noqa: E501

        Boolean flag for enabling/disabling alerting for DataSource  # noqa: E501

        :return: The disable_alerting of this DeviceGroupDataSource.  # noqa: E501
        :rtype: bool
        """
        return self._disable_alerting

    @disable_alerting.setter
    def disable_alerting(self, disable_alerting):
        """Sets the disable_alerting of this DeviceGroupDataSource.

        Boolean flag for enabling/disabling alerting for DataSource  # noqa: E501

        :param disable_alerting: The disable_alerting of this DeviceGroupDataSource.  # noqa: E501
        :type: bool
        """

        self._disable_alerting = disable_alerting

    @property
    def data_source_name(self):
        """Gets the data_source_name of this DeviceGroupDataSource.  # noqa: E501

        The Name of the DataSource  # noqa: E501

        :return: The data_source_name of this DeviceGroupDataSource.  # noqa: E501
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        """Sets the data_source_name of this DeviceGroupDataSource.

        The Name of the DataSource  # noqa: E501

        :param data_source_name: The data_source_name of this DeviceGroupDataSource.  # noqa: E501
        :type: str
        """

        self._data_source_name = data_source_name

    @property
    def data_source_type(self):
        """Gets the data_source_type of this DeviceGroupDataSource.  # noqa: E501

        The Type of the DataSource  # noqa: E501

        :return: The data_source_type of this DeviceGroupDataSource.  # noqa: E501
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        """Sets the data_source_type of this DeviceGroupDataSource.

        The Type of the DataSource  # noqa: E501

        :param data_source_type: The data_source_type of this DeviceGroupDataSource.  # noqa: E501
        :type: str
        """

        self._data_source_type = data_source_type

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
        if issubclass(DeviceGroupDataSource, dict):
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
        if not isinstance(other, DeviceGroupDataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
