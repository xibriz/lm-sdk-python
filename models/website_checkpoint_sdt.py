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
from logicmonitor_sdk.models.sdt import SDT  # noqa: F401,E501

class WebsiteCheckpointSDT(SDT):
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
        'website_name': 'str',
        'checkpoint_name': 'str',
        'checkpoint_id': 'int'
    }
    if hasattr(SDT, "swagger_types"):
        swagger_types.update(SDT.swagger_types)

    attribute_map = {
        'website_name': 'websiteName',
        'checkpoint_name': 'checkpointName',
        'checkpoint_id': 'checkpointId'
    }
    if hasattr(SDT, "attribute_map"):
        attribute_map.update(SDT.attribute_map)

    def __init__(self, website_name=None, checkpoint_name=None, checkpoint_id=None, *args, **kwargs):  # noqa: E501
        """WebsiteCheckpointSDT - a model defined in Swagger"""  # noqa: E501
        self._website_name = None
        self._checkpoint_name = None
        self._checkpoint_id = None
        self.discriminator = None
        if website_name is not None:
            self.website_name = website_name
        if checkpoint_name is not None:
            self.checkpoint_name = checkpoint_name
        if checkpoint_id is not None:
            self.checkpoint_id = checkpoint_id
        SDT.__init__(self, *args, **kwargs)

    @property
    def website_name(self):
        """Gets the website_name of this WebsiteCheckpointSDT.  # noqa: E501


        :return: The website_name of this WebsiteCheckpointSDT.  # noqa: E501
        :rtype: str
        """
        return self._website_name

    @website_name.setter
    def website_name(self, website_name):
        """Sets the website_name of this WebsiteCheckpointSDT.


        :param website_name: The website_name of this WebsiteCheckpointSDT.  # noqa: E501
        :type: str
        """

        self._website_name = website_name

    @property
    def checkpoint_name(self):
        """Gets the checkpoint_name of this WebsiteCheckpointSDT.  # noqa: E501


        :return: The checkpoint_name of this WebsiteCheckpointSDT.  # noqa: E501
        :rtype: str
        """
        return self._checkpoint_name

    @checkpoint_name.setter
    def checkpoint_name(self, checkpoint_name):
        """Sets the checkpoint_name of this WebsiteCheckpointSDT.


        :param checkpoint_name: The checkpoint_name of this WebsiteCheckpointSDT.  # noqa: E501
        :type: str
        """

        self._checkpoint_name = checkpoint_name

    @property
    def checkpoint_id(self):
        """Gets the checkpoint_id of this WebsiteCheckpointSDT.  # noqa: E501


        :return: The checkpoint_id of this WebsiteCheckpointSDT.  # noqa: E501
        :rtype: int
        """
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, checkpoint_id):
        """Sets the checkpoint_id of this WebsiteCheckpointSDT.


        :param checkpoint_id: The checkpoint_id of this WebsiteCheckpointSDT.  # noqa: E501
        :type: int
        """

        self._checkpoint_id = checkpoint_id

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
        if issubclass(WebsiteCheckpointSDT, dict):
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
        if not isinstance(other, WebsiteCheckpointSDT):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
