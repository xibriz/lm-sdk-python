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

class WebsiteCheckpointRawData(object):
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
        'values': 'list[list[object]]',
        'time': 'list[int]',
        'next_page_params': 'str'
    }

    attribute_map = {
        'values': 'values',
        'time': 'time',
        'next_page_params': 'nextPageParams'
    }

    def __init__(self, values=None, time=None, next_page_params=None):  # noqa: E501
        """WebsiteCheckpointRawData - a model defined in Swagger"""  # noqa: E501
        self._values = None
        self._time = None
        self._next_page_params = None
        self.discriminator = None
        if values is not None:
            self.values = values
        if time is not None:
            self.time = time
        if next_page_params is not None:
            self.next_page_params = next_page_params

    @property
    def values(self):
        """Gets the values of this WebsiteCheckpointRawData.  # noqa: E501

        Datapoint values 2-D list  # noqa: E501

        :return: The values of this WebsiteCheckpointRawData.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this WebsiteCheckpointRawData.

        Datapoint values 2-D list  # noqa: E501

        :param values: The values of this WebsiteCheckpointRawData.  # noqa: E501
        :type: list[list[object]]
        """

        self._values = values

    @property
    def time(self):
        """Gets the time of this WebsiteCheckpointRawData.  # noqa: E501

        Timestamp list  # noqa: E501

        :return: The time of this WebsiteCheckpointRawData.  # noqa: E501
        :rtype: list[int]
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this WebsiteCheckpointRawData.

        Timestamp list  # noqa: E501

        :param time: The time of this WebsiteCheckpointRawData.  # noqa: E501
        :type: list[int]
        """

        self._time = time

    @property
    def next_page_params(self):
        """Gets the next_page_params of this WebsiteCheckpointRawData.  # noqa: E501

        The next page parameters  # noqa: E501

        :return: The next_page_params of this WebsiteCheckpointRawData.  # noqa: E501
        :rtype: str
        """
        return self._next_page_params

    @next_page_params.setter
    def next_page_params(self, next_page_params):
        """Sets the next_page_params of this WebsiteCheckpointRawData.

        The next page parameters  # noqa: E501

        :param next_page_params: The next_page_params of this WebsiteCheckpointRawData.  # noqa: E501
        :type: str
        """

        self._next_page_params = next_page_params

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
        if issubclass(WebsiteCheckpointRawData, dict):
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
        if not isinstance(other, WebsiteCheckpointRawData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
