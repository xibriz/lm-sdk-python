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

class VizFilterItem(object):
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
        'name': 'str',
        'label': 'str',
        'type': 'str',
        'inclusion_type': 'str',
        'value': 'list[LabelValuePair]'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'type': 'type',
        'inclusion_type': 'inclusionType',
        'value': 'value'
    }

    def __init__(self, name=None, label=None, type=None, inclusion_type=None, value=None):  # noqa: E501
        """VizFilterItem - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._label = None
        self._type = None
        self._inclusion_type = None
        self._value = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if inclusion_type is not None:
            self.inclusion_type = inclusion_type
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this VizFilterItem.  # noqa: E501


        :return: The name of this VizFilterItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VizFilterItem.


        :param name: The name of this VizFilterItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this VizFilterItem.  # noqa: E501


        :return: The label of this VizFilterItem.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VizFilterItem.


        :param label: The label of this VizFilterItem.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def type(self):
        """Gets the type of this VizFilterItem.  # noqa: E501


        :return: The type of this VizFilterItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VizFilterItem.


        :param type: The type of this VizFilterItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYNONYM", "RESOURCE_PROPERTY"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def inclusion_type(self):
        """Gets the inclusion_type of this VizFilterItem.  # noqa: E501


        :return: The inclusion_type of this VizFilterItem.  # noqa: E501
        :rtype: str
        """
        return self._inclusion_type

    @inclusion_type.setter
    def inclusion_type(self, inclusion_type):
        """Sets the inclusion_type of this VizFilterItem.


        :param inclusion_type: The inclusion_type of this VizFilterItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]  # noqa: E501
        if inclusion_type not in allowed_values:
            raise ValueError(
                "Invalid value for `inclusion_type` ({0}), must be one of {1}"  # noqa: E501
                .format(inclusion_type, allowed_values)
            )

        self._inclusion_type = inclusion_type

    @property
    def value(self):
        """Gets the value of this VizFilterItem.  # noqa: E501


        :return: The value of this VizFilterItem.  # noqa: E501
        :rtype: list[LabelValuePair]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this VizFilterItem.


        :param value: The value of this VizFilterItem.  # noqa: E501
        :type: list[LabelValuePair]
        """

        self._value = value

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
        if issubclass(VizFilterItem, dict):
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
        if not isinstance(other, VizFilterItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
