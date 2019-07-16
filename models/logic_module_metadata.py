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


class LogicModuleMetadata(object):
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
        'lm_locator': 'str',
        'namespace': 'str',
        'quality': 'str',
        'registry_version': 'str'
    }

    attribute_map = {
        'lm_locator': 'lmLocator',
        'namespace': 'namespace',
        'quality': 'quality',
        'registry_version': 'registryVersion'
    }

    def __init__(self, lm_locator=None, namespace=None, quality=None, registry_version=None):  # noqa: E501
        """LogicModuleMetadata - a model defined in Swagger"""  # noqa: E501

        self._lm_locator = None
        self._namespace = None
        self._quality = None
        self._registry_version = None
        self.discriminator = None

        if lm_locator is not None:
            self.lm_locator = lm_locator
        if namespace is not None:
            self.namespace = namespace
        if quality is not None:
            self.quality = quality
        if registry_version is not None:
            self.registry_version = registry_version

    @property
    def lm_locator(self):
        """Gets the lm_locator of this LogicModuleMetadata.  # noqa: E501

        The publication status of this module, along with its \"locator\" token  # noqa: E501

        :return: The lm_locator of this LogicModuleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._lm_locator

    @lm_locator.setter
    def lm_locator(self, lm_locator):
        """Sets the lm_locator of this LogicModuleMetadata.

        The publication status of this module, along with its \"locator\" token  # noqa: E501

        :param lm_locator: The lm_locator of this LogicModuleMetadata.  # noqa: E501
        :type: str
        """

        self._lm_locator = lm_locator

    @property
    def namespace(self):
        """Gets the namespace of this LogicModuleMetadata.  # noqa: E501

        The author of this particular module, which is based on the account name of the form [accountname].logicmonitor.com. As such, the modules are exclusively linked to the individual publisher, not their company's account.  # noqa: E501

        :return: The namespace of this LogicModuleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this LogicModuleMetadata.

        The author of this particular module, which is based on the account name of the form [accountname].logicmonitor.com. As such, the modules are exclusively linked to the individual publisher, not their company's account.  # noqa: E501

        :param namespace: The namespace of this LogicModuleMetadata.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def quality(self):
        """Gets the quality of this LogicModuleMetadata.  # noqa: E501

        The quality specification of this module, as determined by our Monitoring Engineers  # noqa: E501

        :return: The quality of this LogicModuleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this LogicModuleMetadata.

        The quality specification of this module, as determined by our Monitoring Engineers  # noqa: E501

        :param quality: The quality of this LogicModuleMetadata.  # noqa: E501
        :type: str
        """

        self._quality = quality

    @property
    def registry_version(self):
        """Gets the registry_version of this LogicModuleMetadata.  # noqa: E501

        Indicates the specific version of this module  # noqa: E501

        :return: The registry_version of this LogicModuleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._registry_version

    @registry_version.setter
    def registry_version(self, registry_version):
        """Sets the registry_version of this LogicModuleMetadata.

        Indicates the specific version of this module  # noqa: E501

        :param registry_version: The registry_version of this LogicModuleMetadata.  # noqa: E501
        :type: str
        """

        self._registry_version = registry_version

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
        if issubclass(LogicModuleMetadata, dict):
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
        if not isinstance(other, LogicModuleMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
