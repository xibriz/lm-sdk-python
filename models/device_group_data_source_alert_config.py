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

from logicmonitor_sdk.models.device_group_data_source_data_point_config import DeviceGroupDataSourceDataPointConfig  # noqa: F401,E501


class DeviceGroupDataSourceAlertConfig(object):
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
        'datasource_type': 'str',
        'dp_config': 'list[DeviceGroupDataSourceDataPointConfig]'
    }

    attribute_map = {
        'datasource_type': 'datasourceType',
        'dp_config': 'dpConfig'
    }

    def __init__(self, datasource_type=None, dp_config=None):  # noqa: E501
        """DeviceGroupDataSourceAlertConfig - a model defined in Swagger"""  # noqa: E501

        self._datasource_type = None
        self._dp_config = None
        self.discriminator = None

        if datasource_type is not None:
            self.datasource_type = datasource_type
        if dp_config is not None:
            self.dp_config = dp_config

    @property
    def datasource_type(self):
        """Gets the datasource_type of this DeviceGroupDataSourceAlertConfig.  # noqa: E501


        :return: The datasource_type of this DeviceGroupDataSourceAlertConfig.  # noqa: E501
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        """Sets the datasource_type of this DeviceGroupDataSourceAlertConfig.


        :param datasource_type: The datasource_type of this DeviceGroupDataSourceAlertConfig.  # noqa: E501
        :type: str
        """

        self._datasource_type = datasource_type

    @property
    def dp_config(self):
        """Gets the dp_config of this DeviceGroupDataSourceAlertConfig.  # noqa: E501


        :return: The dp_config of this DeviceGroupDataSourceAlertConfig.  # noqa: E501
        :rtype: list[DeviceGroupDataSourceDataPointConfig]
        """
        return self._dp_config

    @dp_config.setter
    def dp_config(self, dp_config):
        """Sets the dp_config of this DeviceGroupDataSourceAlertConfig.


        :param dp_config: The dp_config of this DeviceGroupDataSourceAlertConfig.  # noqa: E501
        :type: list[DeviceGroupDataSourceDataPointConfig]
        """

        self._dp_config = dp_config

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
        if issubclass(DeviceGroupDataSourceAlertConfig, dict):
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
        if not isinstance(other, DeviceGroupDataSourceAlertConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
