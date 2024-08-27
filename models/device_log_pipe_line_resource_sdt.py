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

class DeviceLogPipeLineResourceSDT(SDT):
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
        'device_log_pipe_line_resource_id': 'int',
        'log_pipe_line_name': 'str',
        'device_id': 'int',
        'device_display_name': 'str'
    }
    if hasattr(SDT, "swagger_types"):
        swagger_types.update(SDT.swagger_types)

    attribute_map = {
        'device_log_pipe_line_resource_id': 'deviceLogPipeLineResourceId',
        'log_pipe_line_name': 'logPipeLineName',
        'device_id': 'deviceId',
        'device_display_name': 'deviceDisplayName'
    }
    if hasattr(SDT, "attribute_map"):
        attribute_map.update(SDT.attribute_map)

    def __init__(self, device_log_pipe_line_resource_id=None, log_pipe_line_name=None, device_id=None, device_display_name=None, *args, **kwargs):  # noqa: E501
        """DeviceLogPipeLineResourceSDT - a model defined in Swagger"""  # noqa: E501
        self._device_log_pipe_line_resource_id = None
        self._log_pipe_line_name = None
        self._device_id = None
        self._device_display_name = None
        self.discriminator = None
        if device_log_pipe_line_resource_id is not None:
            self.device_log_pipe_line_resource_id = device_log_pipe_line_resource_id
        if log_pipe_line_name is not None:
            self.log_pipe_line_name = log_pipe_line_name
        if device_id is not None:
            self.device_id = device_id
        if device_display_name is not None:
            self.device_display_name = device_display_name
        SDT.__init__(self, *args, **kwargs)

    @property
    def device_log_pipe_line_resource_id(self):
        """Gets the device_log_pipe_line_resource_id of this DeviceLogPipeLineResourceSDT.  # noqa: E501

        The id of the device logPipeLineResource that the SDT will be associated with  # noqa: E501

        :return: The device_log_pipe_line_resource_id of this DeviceLogPipeLineResourceSDT.  # noqa: E501
        :rtype: int
        """
        return self._device_log_pipe_line_resource_id

    @device_log_pipe_line_resource_id.setter
    def device_log_pipe_line_resource_id(self, device_log_pipe_line_resource_id):
        """Sets the device_log_pipe_line_resource_id of this DeviceLogPipeLineResourceSDT.

        The id of the device logPipeLineResource that the SDT will be associated with  # noqa: E501

        :param device_log_pipe_line_resource_id: The device_log_pipe_line_resource_id of this DeviceLogPipeLineResourceSDT.  # noqa: E501
        :type: int
        """

        self._device_log_pipe_line_resource_id = device_log_pipe_line_resource_id

    @property
    def log_pipe_line_name(self):
        """Gets the log_pipe_line_name of this DeviceLogPipeLineResourceSDT.  # noqa: E501

        The name of the pipe line that the SDT will apply to  # noqa: E501

        :return: The log_pipe_line_name of this DeviceLogPipeLineResourceSDT.  # noqa: E501
        :rtype: str
        """
        return self._log_pipe_line_name

    @log_pipe_line_name.setter
    def log_pipe_line_name(self, log_pipe_line_name):
        """Sets the log_pipe_line_name of this DeviceLogPipeLineResourceSDT.

        The name of the pipe line that the SDT will apply to  # noqa: E501

        :param log_pipe_line_name: The log_pipe_line_name of this DeviceLogPipeLineResourceSDT.  # noqa: E501
        :type: str
        """

        self._log_pipe_line_name = log_pipe_line_name

    @property
    def device_id(self):
        """Gets the device_id of this DeviceLogPipeLineResourceSDT.  # noqa: E501

        The id of the device associated with the pipe line that the SDT will apply to  # noqa: E501

        :return: The device_id of this DeviceLogPipeLineResourceSDT.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DeviceLogPipeLineResourceSDT.

        The id of the device associated with the pipe line that the SDT will apply to  # noqa: E501

        :param device_id: The device_id of this DeviceLogPipeLineResourceSDT.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def device_display_name(self):
        """Gets the device_display_name of this DeviceLogPipeLineResourceSDT.  # noqa: E501

        The display name of the device associated with the logPipeLine that the SDT will apply to  # noqa: E501

        :return: The device_display_name of this DeviceLogPipeLineResourceSDT.  # noqa: E501
        :rtype: str
        """
        return self._device_display_name

    @device_display_name.setter
    def device_display_name(self, device_display_name):
        """Sets the device_display_name of this DeviceLogPipeLineResourceSDT.

        The display name of the device associated with the logPipeLine that the SDT will apply to  # noqa: E501

        :param device_display_name: The device_display_name of this DeviceLogPipeLineResourceSDT.  # noqa: E501
        :type: str
        """

        self._device_display_name = device_display_name

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
        if issubclass(DeviceLogPipeLineResourceSDT, dict):
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
        if not isinstance(other, DeviceLogPipeLineResourceSDT):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
