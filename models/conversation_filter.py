# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. <br> <br> Note: <ul> <li> For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. </li> <li> Both underscore and camelCase are supported if parameters are encapsulated within the body. </li> <li> Only camelCase is supported if parameters are encapsulated within the body and also if the user is passing raw JSON as REQUEST parameter. However, the RESPONSE parameters always contain an underscore. For example, you can use testLocation or test_location in the REQUEST parameter. But the RESPONSE parameter will always be test_location. </li> <li> The fields parameter only supports camelCase. </li> </ul>  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConversationFilter(object):
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
        'from_operator': 'str',
        'from_endpoint': 'str',
        'to_endpoint': 'str',
        'to_operator': 'str',
        'include_or_exclude': 'str'
    }

    attribute_map = {
        'from_operator': 'fromOperator',
        'from_endpoint': 'fromEndpoint',
        'to_endpoint': 'toEndpoint',
        'to_operator': 'toOperator',
        'include_or_exclude': 'includeOrExclude'
    }

    def __init__(self, from_operator=None, from_endpoint=None, to_endpoint=None, to_operator=None, include_or_exclude=None):  # noqa: E501
        """ConversationFilter - a model defined in Swagger"""  # noqa: E501
        self._from_operator = None
        self._from_endpoint = None
        self._to_endpoint = None
        self._to_operator = None
        self._include_or_exclude = None
        self.discriminator = None
        if from_operator is not None:
            self.from_operator = from_operator
        if from_endpoint is not None:
            self.from_endpoint = from_endpoint
        if to_endpoint is not None:
            self.to_endpoint = to_endpoint
        if to_operator is not None:
            self.to_operator = to_operator
        if include_or_exclude is not None:
            self.include_or_exclude = include_or_exclude

    @property
    def from_operator(self):
        """Gets the from_operator of this ConversationFilter.  # noqa: E501


        :return: The from_operator of this ConversationFilter.  # noqa: E501
        :rtype: str
        """
        return self._from_operator

    @from_operator.setter
    def from_operator(self, from_operator):
        """Sets the from_operator of this ConversationFilter.


        :param from_operator: The from_operator of this ConversationFilter.  # noqa: E501
        :type: str
        """

        self._from_operator = from_operator

    @property
    def from_endpoint(self):
        """Gets the from_endpoint of this ConversationFilter.  # noqa: E501


        :return: The from_endpoint of this ConversationFilter.  # noqa: E501
        :rtype: str
        """
        return self._from_endpoint

    @from_endpoint.setter
    def from_endpoint(self, from_endpoint):
        """Sets the from_endpoint of this ConversationFilter.


        :param from_endpoint: The from_endpoint of this ConversationFilter.  # noqa: E501
        :type: str
        """

        self._from_endpoint = from_endpoint

    @property
    def to_endpoint(self):
        """Gets the to_endpoint of this ConversationFilter.  # noqa: E501


        :return: The to_endpoint of this ConversationFilter.  # noqa: E501
        :rtype: str
        """
        return self._to_endpoint

    @to_endpoint.setter
    def to_endpoint(self, to_endpoint):
        """Sets the to_endpoint of this ConversationFilter.


        :param to_endpoint: The to_endpoint of this ConversationFilter.  # noqa: E501
        :type: str
        """

        self._to_endpoint = to_endpoint

    @property
    def to_operator(self):
        """Gets the to_operator of this ConversationFilter.  # noqa: E501


        :return: The to_operator of this ConversationFilter.  # noqa: E501
        :rtype: str
        """
        return self._to_operator

    @to_operator.setter
    def to_operator(self, to_operator):
        """Sets the to_operator of this ConversationFilter.


        :param to_operator: The to_operator of this ConversationFilter.  # noqa: E501
        :type: str
        """

        self._to_operator = to_operator

    @property
    def include_or_exclude(self):
        """Gets the include_or_exclude of this ConversationFilter.  # noqa: E501


        :return: The include_or_exclude of this ConversationFilter.  # noqa: E501
        :rtype: str
        """
        return self._include_or_exclude

    @include_or_exclude.setter
    def include_or_exclude(self, include_or_exclude):
        """Sets the include_or_exclude of this ConversationFilter.


        :param include_or_exclude: The include_or_exclude of this ConversationFilter.  # noqa: E501
        :type: str
        """

        self._include_or_exclude = include_or_exclude

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
        if issubclass(ConversationFilter, dict):
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
        if not isinstance(other, ConversationFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
