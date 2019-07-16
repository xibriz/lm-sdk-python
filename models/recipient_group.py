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

from logicmonitor_sdk.models.recipient import Recipient  # noqa: F401,E501


class RecipientGroup(object):
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
        'description': 'str',
        'group_name': 'str',
        'id': 'int',
        'recipients': 'list[Recipient]'
    }

    attribute_map = {
        'description': 'description',
        'group_name': 'groupName',
        'id': 'id',
        'recipients': 'recipients'
    }

    def __init__(self, description=None, group_name=None, id=None, recipients=None):  # noqa: E501
        """RecipientGroup - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._group_name = None
        self._id = None
        self._recipients = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.group_name = group_name
        if id is not None:
            self.id = id
        if recipients is not None:
            self.recipients = recipients

    @property
    def description(self):
        """Gets the description of this RecipientGroup.  # noqa: E501

        The description of the recipient group  # noqa: E501

        :return: The description of this RecipientGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RecipientGroup.

        The description of the recipient group  # noqa: E501

        :param description: The description of this RecipientGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def group_name(self):
        """Gets the group_name of this RecipientGroup.  # noqa: E501

        The name of the recipient group  # noqa: E501

        :return: The group_name of this RecipientGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this RecipientGroup.

        The name of the recipient group  # noqa: E501

        :param group_name: The group_name of this RecipientGroup.  # noqa: E501
        :type: str
        """
        if group_name is None:
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def id(self):
        """Gets the id of this RecipientGroup.  # noqa: E501


        :return: The id of this RecipientGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecipientGroup.


        :param id: The id of this RecipientGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def recipients(self):
        """Gets the recipients of this RecipientGroup.  # noqa: E501

        The recipients in the group  # noqa: E501

        :return: The recipients of this RecipientGroup.  # noqa: E501
        :rtype: list[Recipient]
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this RecipientGroup.

        The recipients in the group  # noqa: E501

        :param recipients: The recipients of this RecipientGroup.  # noqa: E501
        :type: list[Recipient]
        """

        self._recipients = recipients

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
        if issubclass(RecipientGroup, dict):
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
        if not isinstance(other, RecipientGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
