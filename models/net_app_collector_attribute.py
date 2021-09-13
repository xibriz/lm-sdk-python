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

from logicmonitor_sdk.models.collector_attribute import CollectorAttribute  # noqa: F401,E501


class NetAppCollectorAttribute(CollectorAttribute):
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
        'net_app_type': 'str',
        'ip': 'str',
        'net_app_instance': 'str',
        'net_app_xml_bulk_locator': 'str',
        'net_app_xml': 'str',
        'net_app_api': 'str',
        'params': 'object',
        'net_app_aggregate': 'str',
        'net_app_xml_index': 'str',
        'net_app_xml_instance': 'str',
        'net_app_index': 'str',
        'net_app_xml_bulk': 'str',
        'net_app_object': 'str',
        'net_app_xml_locator': 'str'
    }

    attribute_map = {
        'name': 'name',
        'net_app_type': 'netAppType',
        'ip': 'ip',
        'net_app_instance': 'netAppInstance',
        'net_app_xml_bulk_locator': 'netAppXMLBulkLocator',
        'net_app_xml': 'netAppXML',
        'net_app_api': 'netAppAPI',
        'params': 'params',
        'net_app_aggregate': 'netAppAggregate',
        'net_app_xml_index': 'netAppXMLIndex',
        'net_app_xml_instance': 'netAppXMLInstance',
        'net_app_index': 'netAppIndex',
        'net_app_xml_bulk': 'netAppXMLBulk',
        'net_app_object': 'netAppObject',
        'net_app_xml_locator': 'netAppXMLLocator'
    }

    def __init__(self, name=None, net_app_type=None, ip=None, net_app_instance=None, net_app_xml_bulk_locator=None, net_app_xml=None, net_app_api=None, params=None, net_app_aggregate=None, net_app_xml_index=None, net_app_xml_instance=None, net_app_index=None, net_app_xml_bulk=None, net_app_object=None, net_app_xml_locator=None):  # noqa: E501
        """NetAppCollectorAttribute - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._net_app_type = None
        self._ip = None
        self._net_app_instance = None
        self._net_app_xml_bulk_locator = None
        self._net_app_xml = None
        self._net_app_api = None
        self._params = None
        self._net_app_aggregate = None
        self._net_app_xml_index = None
        self._net_app_xml_instance = None
        self._net_app_index = None
        self._net_app_xml_bulk = None
        self._net_app_object = None
        self._net_app_xml_locator = None
        self.discriminator = None

        self.name = name
        if net_app_type is not None:
            self.net_app_type = net_app_type
        if ip is not None:
            self.ip = ip
        if net_app_instance is not None:
            self.net_app_instance = net_app_instance
        if net_app_xml_bulk_locator is not None:
            self.net_app_xml_bulk_locator = net_app_xml_bulk_locator
        if net_app_xml is not None:
            self.net_app_xml = net_app_xml
        if net_app_api is not None:
            self.net_app_api = net_app_api
        if params is not None:
            self.params = params
        if net_app_aggregate is not None:
            self.net_app_aggregate = net_app_aggregate
        if net_app_xml_index is not None:
            self.net_app_xml_index = net_app_xml_index
        if net_app_xml_instance is not None:
            self.net_app_xml_instance = net_app_xml_instance
        if net_app_index is not None:
            self.net_app_index = net_app_index
        if net_app_xml_bulk is not None:
            self.net_app_xml_bulk = net_app_xml_bulk
        if net_app_object is not None:
            self.net_app_object = net_app_object
        if net_app_xml_locator is not None:
            self.net_app_xml_locator = net_app_xml_locator

    @property
    def name(self):
        """Gets the name of this NetAppCollectorAttribute.  # noqa: E501


        :return: The name of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetAppCollectorAttribute.


        :param name: The name of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def net_app_type(self):
        """Gets the net_app_type of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_type of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_type

    @net_app_type.setter
    def net_app_type(self, net_app_type):
        """Sets the net_app_type of this NetAppCollectorAttribute.


        :param net_app_type: The net_app_type of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_type = net_app_type

    @property
    def ip(self):
        """Gets the ip of this NetAppCollectorAttribute.  # noqa: E501


        :return: The ip of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this NetAppCollectorAttribute.


        :param ip: The ip of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def net_app_instance(self):
        """Gets the net_app_instance of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_instance of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_instance

    @net_app_instance.setter
    def net_app_instance(self, net_app_instance):
        """Sets the net_app_instance of this NetAppCollectorAttribute.


        :param net_app_instance: The net_app_instance of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_instance = net_app_instance

    @property
    def net_app_xml_bulk_locator(self):
        """Gets the net_app_xml_bulk_locator of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_xml_bulk_locator of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_xml_bulk_locator

    @net_app_xml_bulk_locator.setter
    def net_app_xml_bulk_locator(self, net_app_xml_bulk_locator):
        """Sets the net_app_xml_bulk_locator of this NetAppCollectorAttribute.


        :param net_app_xml_bulk_locator: The net_app_xml_bulk_locator of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_xml_bulk_locator = net_app_xml_bulk_locator

    @property
    def net_app_xml(self):
        """Gets the net_app_xml of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_xml of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_xml

    @net_app_xml.setter
    def net_app_xml(self, net_app_xml):
        """Sets the net_app_xml of this NetAppCollectorAttribute.


        :param net_app_xml: The net_app_xml of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_xml = net_app_xml

    @property
    def net_app_api(self):
        """Gets the net_app_api of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_api of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_api

    @net_app_api.setter
    def net_app_api(self, net_app_api):
        """Sets the net_app_api of this NetAppCollectorAttribute.


        :param net_app_api: The net_app_api of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_api = net_app_api

    @property
    def params(self):
        """Gets the params of this NetAppCollectorAttribute.  # noqa: E501


        :return: The params of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this NetAppCollectorAttribute.


        :param params: The params of this NetAppCollectorAttribute.  # noqa: E501
        :type: object
        """

        self._params = params

    @property
    def net_app_aggregate(self):
        """Gets the net_app_aggregate of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_aggregate of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_aggregate

    @net_app_aggregate.setter
    def net_app_aggregate(self, net_app_aggregate):
        """Sets the net_app_aggregate of this NetAppCollectorAttribute.


        :param net_app_aggregate: The net_app_aggregate of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_aggregate = net_app_aggregate

    @property
    def net_app_xml_index(self):
        """Gets the net_app_xml_index of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_xml_index of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_xml_index

    @net_app_xml_index.setter
    def net_app_xml_index(self, net_app_xml_index):
        """Sets the net_app_xml_index of this NetAppCollectorAttribute.


        :param net_app_xml_index: The net_app_xml_index of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_xml_index = net_app_xml_index

    @property
    def net_app_xml_instance(self):
        """Gets the net_app_xml_instance of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_xml_instance of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_xml_instance

    @net_app_xml_instance.setter
    def net_app_xml_instance(self, net_app_xml_instance):
        """Sets the net_app_xml_instance of this NetAppCollectorAttribute.


        :param net_app_xml_instance: The net_app_xml_instance of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_xml_instance = net_app_xml_instance

    @property
    def net_app_index(self):
        """Gets the net_app_index of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_index of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_index

    @net_app_index.setter
    def net_app_index(self, net_app_index):
        """Sets the net_app_index of this NetAppCollectorAttribute.


        :param net_app_index: The net_app_index of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_index = net_app_index

    @property
    def net_app_xml_bulk(self):
        """Gets the net_app_xml_bulk of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_xml_bulk of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_xml_bulk

    @net_app_xml_bulk.setter
    def net_app_xml_bulk(self, net_app_xml_bulk):
        """Sets the net_app_xml_bulk of this NetAppCollectorAttribute.


        :param net_app_xml_bulk: The net_app_xml_bulk of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_xml_bulk = net_app_xml_bulk

    @property
    def net_app_object(self):
        """Gets the net_app_object of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_object of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_object

    @net_app_object.setter
    def net_app_object(self, net_app_object):
        """Sets the net_app_object of this NetAppCollectorAttribute.


        :param net_app_object: The net_app_object of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_object = net_app_object

    @property
    def net_app_xml_locator(self):
        """Gets the net_app_xml_locator of this NetAppCollectorAttribute.  # noqa: E501


        :return: The net_app_xml_locator of this NetAppCollectorAttribute.  # noqa: E501
        :rtype: str
        """
        return self._net_app_xml_locator

    @net_app_xml_locator.setter
    def net_app_xml_locator(self, net_app_xml_locator):
        """Sets the net_app_xml_locator of this NetAppCollectorAttribute.


        :param net_app_xml_locator: The net_app_xml_locator of this NetAppCollectorAttribute.  # noqa: E501
        :type: str
        """

        self._net_app_xml_locator = net_app_xml_locator

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
        if issubclass(NetAppCollectorAttribute, dict):
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
        if not isinstance(other, NetAppCollectorAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
