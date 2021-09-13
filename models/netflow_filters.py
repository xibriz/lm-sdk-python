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

from logicmonitor_sdk.models.conversation_filter import ConversationFilter  # noqa: F401,E501


class NetflowFilters(object):
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
        'node_b': 'str',
        'protocol': 'str',
        'ip_version': 'str',
        'top': 'int',
        'if_idx': 'int',
        'if_name': 'str',
        'qos_type': 'str',
        'ports': 'str',
        'node_a': 'str',
        'conversation': 'list[ConversationFilter]',
        'direction': 'str'
    }

    attribute_map = {
        'node_b': 'nodeB',
        'protocol': 'protocol',
        'ip_version': 'ipVersion',
        'top': 'top',
        'if_idx': 'ifIdx',
        'if_name': 'ifName',
        'qos_type': 'qosType',
        'ports': 'ports',
        'node_a': 'nodeA',
        'conversation': 'conversation',
        'direction': 'direction'
    }

    def __init__(self, node_b=None, protocol=None, ip_version=None, top=None, if_idx=None, if_name=None, qos_type=None, ports=None, node_a=None, conversation=None, direction=None):  # noqa: E501
        """NetflowFilters - a model defined in Swagger"""  # noqa: E501

        self._node_b = None
        self._protocol = None
        self._ip_version = None
        self._top = None
        self._if_idx = None
        self._if_name = None
        self._qos_type = None
        self._ports = None
        self._node_a = None
        self._conversation = None
        self._direction = None
        self.discriminator = None

        if node_b is not None:
            self.node_b = node_b
        if protocol is not None:
            self.protocol = protocol
        if ip_version is not None:
            self.ip_version = ip_version
        if top is not None:
            self.top = top
        if if_idx is not None:
            self.if_idx = if_idx
        if if_name is not None:
            self.if_name = if_name
        if qos_type is not None:
            self.qos_type = qos_type
        if ports is not None:
            self.ports = ports
        if node_a is not None:
            self.node_a = node_a
        if conversation is not None:
            self.conversation = conversation
        if direction is not None:
            self.direction = direction

    @property
    def node_b(self):
        """Gets the node_b of this NetflowFilters.  # noqa: E501


        :return: The node_b of this NetflowFilters.  # noqa: E501
        :rtype: str
        """
        return self._node_b

    @node_b.setter
    def node_b(self, node_b):
        """Sets the node_b of this NetflowFilters.


        :param node_b: The node_b of this NetflowFilters.  # noqa: E501
        :type: str
        """

        self._node_b = node_b

    @property
    def protocol(self):
        """Gets the protocol of this NetflowFilters.  # noqa: E501


        :return: The protocol of this NetflowFilters.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NetflowFilters.


        :param protocol: The protocol of this NetflowFilters.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def ip_version(self):
        """Gets the ip_version of this NetflowFilters.  # noqa: E501


        :return: The ip_version of this NetflowFilters.  # noqa: E501
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this NetflowFilters.


        :param ip_version: The ip_version of this NetflowFilters.  # noqa: E501
        :type: str
        """

        self._ip_version = ip_version

    @property
    def top(self):
        """Gets the top of this NetflowFilters.  # noqa: E501


        :return: The top of this NetflowFilters.  # noqa: E501
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this NetflowFilters.


        :param top: The top of this NetflowFilters.  # noqa: E501
        :type: int
        """

        self._top = top

    @property
    def if_idx(self):
        """Gets the if_idx of this NetflowFilters.  # noqa: E501


        :return: The if_idx of this NetflowFilters.  # noqa: E501
        :rtype: int
        """
        return self._if_idx

    @if_idx.setter
    def if_idx(self, if_idx):
        """Sets the if_idx of this NetflowFilters.


        :param if_idx: The if_idx of this NetflowFilters.  # noqa: E501
        :type: int
        """

        self._if_idx = if_idx

    @property
    def if_name(self):
        """Gets the if_name of this NetflowFilters.  # noqa: E501


        :return: The if_name of this NetflowFilters.  # noqa: E501
        :rtype: str
        """
        return self._if_name

    @if_name.setter
    def if_name(self, if_name):
        """Sets the if_name of this NetflowFilters.


        :param if_name: The if_name of this NetflowFilters.  # noqa: E501
        :type: str
        """

        self._if_name = if_name

    @property
    def qos_type(self):
        """Gets the qos_type of this NetflowFilters.  # noqa: E501


        :return: The qos_type of this NetflowFilters.  # noqa: E501
        :rtype: str
        """
        return self._qos_type

    @qos_type.setter
    def qos_type(self, qos_type):
        """Sets the qos_type of this NetflowFilters.


        :param qos_type: The qos_type of this NetflowFilters.  # noqa: E501
        :type: str
        """

        self._qos_type = qos_type

    @property
    def ports(self):
        """Gets the ports of this NetflowFilters.  # noqa: E501


        :return: The ports of this NetflowFilters.  # noqa: E501
        :rtype: str
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this NetflowFilters.


        :param ports: The ports of this NetflowFilters.  # noqa: E501
        :type: str
        """

        self._ports = ports

    @property
    def node_a(self):
        """Gets the node_a of this NetflowFilters.  # noqa: E501


        :return: The node_a of this NetflowFilters.  # noqa: E501
        :rtype: str
        """
        return self._node_a

    @node_a.setter
    def node_a(self, node_a):
        """Sets the node_a of this NetflowFilters.


        :param node_a: The node_a of this NetflowFilters.  # noqa: E501
        :type: str
        """

        self._node_a = node_a

    @property
    def conversation(self):
        """Gets the conversation of this NetflowFilters.  # noqa: E501


        :return: The conversation of this NetflowFilters.  # noqa: E501
        :rtype: list[ConversationFilter]
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        """Sets the conversation of this NetflowFilters.


        :param conversation: The conversation of this NetflowFilters.  # noqa: E501
        :type: list[ConversationFilter]
        """

        self._conversation = conversation

    @property
    def direction(self):
        """Gets the direction of this NetflowFilters.  # noqa: E501


        :return: The direction of this NetflowFilters.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this NetflowFilters.


        :param direction: The direction of this NetflowFilters.  # noqa: E501
        :type: str
        """

        self._direction = direction

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
        if issubclass(NetflowFilters, dict):
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
        if not isinstance(other, NetflowFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
