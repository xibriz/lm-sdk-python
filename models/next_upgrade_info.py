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


class NextUpgradeInfo(object):
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
        'major_version': 'int',
        'mandatory': 'bool',
        'minor_version': 'int',
        'stable': 'bool',
        'upgrade_time': 'str',
        'upgrade_time_epoch': 'int'
    }

    attribute_map = {
        'major_version': 'majorVersion',
        'mandatory': 'mandatory',
        'minor_version': 'minorVersion',
        'stable': 'stable',
        'upgrade_time': 'upgradeTime',
        'upgrade_time_epoch': 'upgradeTimeEpoch'
    }

    def __init__(self, major_version=None, mandatory=None, minor_version=None, stable=None, upgrade_time=None, upgrade_time_epoch=None):  # noqa: E501
        """NextUpgradeInfo - a model defined in Swagger"""  # noqa: E501

        self._major_version = None
        self._mandatory = None
        self._minor_version = None
        self._stable = None
        self._upgrade_time = None
        self._upgrade_time_epoch = None
        self.discriminator = None

        if major_version is not None:
            self.major_version = major_version
        if mandatory is not None:
            self.mandatory = mandatory
        if minor_version is not None:
            self.minor_version = minor_version
        if stable is not None:
            self.stable = stable
        if upgrade_time is not None:
            self.upgrade_time = upgrade_time
        if upgrade_time_epoch is not None:
            self.upgrade_time_epoch = upgrade_time_epoch

    @property
    def major_version(self):
        """Gets the major_version of this NextUpgradeInfo.  # noqa: E501


        :return: The major_version of this NextUpgradeInfo.  # noqa: E501
        :rtype: int
        """
        return self._major_version

    @major_version.setter
    def major_version(self, major_version):
        """Sets the major_version of this NextUpgradeInfo.


        :param major_version: The major_version of this NextUpgradeInfo.  # noqa: E501
        :type: int
        """

        self._major_version = major_version

    @property
    def mandatory(self):
        """Gets the mandatory of this NextUpgradeInfo.  # noqa: E501


        :return: The mandatory of this NextUpgradeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this NextUpgradeInfo.


        :param mandatory: The mandatory of this NextUpgradeInfo.  # noqa: E501
        :type: bool
        """

        self._mandatory = mandatory

    @property
    def minor_version(self):
        """Gets the minor_version of this NextUpgradeInfo.  # noqa: E501


        :return: The minor_version of this NextUpgradeInfo.  # noqa: E501
        :rtype: int
        """
        return self._minor_version

    @minor_version.setter
    def minor_version(self, minor_version):
        """Sets the minor_version of this NextUpgradeInfo.


        :param minor_version: The minor_version of this NextUpgradeInfo.  # noqa: E501
        :type: int
        """

        self._minor_version = minor_version

    @property
    def stable(self):
        """Gets the stable of this NextUpgradeInfo.  # noqa: E501


        :return: The stable of this NextUpgradeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._stable

    @stable.setter
    def stable(self, stable):
        """Sets the stable of this NextUpgradeInfo.


        :param stable: The stable of this NextUpgradeInfo.  # noqa: E501
        :type: bool
        """

        self._stable = stable

    @property
    def upgrade_time(self):
        """Gets the upgrade_time of this NextUpgradeInfo.  # noqa: E501


        :return: The upgrade_time of this NextUpgradeInfo.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_time

    @upgrade_time.setter
    def upgrade_time(self, upgrade_time):
        """Sets the upgrade_time of this NextUpgradeInfo.


        :param upgrade_time: The upgrade_time of this NextUpgradeInfo.  # noqa: E501
        :type: str
        """

        self._upgrade_time = upgrade_time

    @property
    def upgrade_time_epoch(self):
        """Gets the upgrade_time_epoch of this NextUpgradeInfo.  # noqa: E501


        :return: The upgrade_time_epoch of this NextUpgradeInfo.  # noqa: E501
        :rtype: int
        """
        return self._upgrade_time_epoch

    @upgrade_time_epoch.setter
    def upgrade_time_epoch(self, upgrade_time_epoch):
        """Sets the upgrade_time_epoch of this NextUpgradeInfo.


        :param upgrade_time_epoch: The upgrade_time_epoch of this NextUpgradeInfo.  # noqa: E501
        :type: int
        """

        self._upgrade_time_epoch = upgrade_time_epoch

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
        if issubclass(NextUpgradeInfo, dict):
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
        if not isinstance(other, NextUpgradeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
