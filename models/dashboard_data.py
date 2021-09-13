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


class DashboardData(object):
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
        'user_permission': 'str',
        'name': 'str',
        'sharable': 'bool',
        'id': 'int'
    }

    attribute_map = {
        'user_permission': 'userPermission',
        'name': 'name',
        'sharable': 'sharable',
        'id': 'id'
    }

    def __init__(self, user_permission=None, name=None, sharable=None, id=None):  # noqa: E501
        """DashboardData - a model defined in Swagger"""  # noqa: E501

        self._user_permission = None
        self._name = None
        self._sharable = None
        self._id = None
        self.discriminator = None

        if user_permission is not None:
            self.user_permission = user_permission
        if name is not None:
            self.name = name
        if sharable is not None:
            self.sharable = sharable
        if id is not None:
            self.id = id

    @property
    def user_permission(self):
        """Gets the user_permission of this DashboardData.  # noqa: E501


        :return: The user_permission of this DashboardData.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this DashboardData.


        :param user_permission: The user_permission of this DashboardData.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

    @property
    def name(self):
        """Gets the name of this DashboardData.  # noqa: E501


        :return: The name of this DashboardData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardData.


        :param name: The name of this DashboardData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sharable(self):
        """Gets the sharable of this DashboardData.  # noqa: E501


        :return: The sharable of this DashboardData.  # noqa: E501
        :rtype: bool
        """
        return self._sharable

    @sharable.setter
    def sharable(self, sharable):
        """Sets the sharable of this DashboardData.


        :param sharable: The sharable of this DashboardData.  # noqa: E501
        :type: bool
        """

        self._sharable = sharable

    @property
    def id(self):
        """Gets the id of this DashboardData.  # noqa: E501


        :return: The id of this DashboardData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DashboardData.


        :param id: The id of this DashboardData.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(DashboardData, dict):
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
        if not isinstance(other, DashboardData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
