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


class MatchPattern(object):
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
        'alert_level': 'str',
        'pattern': 'str'
    }

    attribute_map = {
        'alert_level': 'alertLevel',
        'pattern': 'pattern'
    }

    def __init__(self, alert_level=None, pattern=None):  # noqa: E501
        """MatchPattern - a model defined in Swagger"""  # noqa: E501

        self._alert_level = None
        self._pattern = None
        self.discriminator = None

        if alert_level is not None:
            self.alert_level = alert_level
        if pattern is not None:
            self.pattern = pattern

    @property
    def alert_level(self):
        """Gets the alert_level of this MatchPattern.  # noqa: E501

        The level of alert to trigger: warn | error | critical  # noqa: E501

        :return: The alert_level of this MatchPattern.  # noqa: E501
        :rtype: str
        """
        return self._alert_level

    @alert_level.setter
    def alert_level(self, alert_level):
        """Sets the alert_level of this MatchPattern.

        The level of alert to trigger: warn | error | critical  # noqa: E501

        :param alert_level: The alert_level of this MatchPattern.  # noqa: E501
        :type: str
        """

        self._alert_level = alert_level

    @property
    def pattern(self):
        """Gets the pattern of this MatchPattern.  # noqa: E501

        The regex or plain text to look for in the file and trigger alert if found  # noqa: E501

        :return: The pattern of this MatchPattern.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this MatchPattern.

        The regex or plain text to look for in the file and trigger alert if found  # noqa: E501

        :param pattern: The pattern of this MatchPattern.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

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
        if issubclass(MatchPattern, dict):
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
        if not isinstance(other, MatchPattern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
