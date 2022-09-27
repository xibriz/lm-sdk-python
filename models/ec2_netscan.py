# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.ec2_ddr import Ec2DDR  # noqa: F401,E501
from logicmonitor_sdk.models.ec2_netscan_policy_credential import EC2NetscanPolicyCredential  # noqa: F401,E501
from logicmonitor_sdk.models.exclude_duplicate_ips import ExcludeDuplicateIps  # noqa: F401,E501
from logicmonitor_sdk.models.netscan import Netscan  # noqa: F401,E501
from logicmonitor_sdk.models.rest_netscan_ports import RestNetscanPorts  # noqa: F401,E501
from logicmonitor_sdk.models.rest_schedule import RestSchedule  # noqa: F401,E501


class Ec2Netscan(Netscan):
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
        'creator': 'str',
        'collector_group_name': 'str',
        'method': 'str',
        'collector_group': 'int',
        'description': 'str',
        'next_start': 'str',
        'duplicate': 'ExcludeDuplicateIps',
        'version': 'int',
        'collector': 'int',
        'ignore_system_i_ps_duplicates': 'bool',
        'schedule': 'RestSchedule',
        'collector_description': 'str',
        'name': 'str',
        'next_start_epoch': 'int',
        'id': 'int',
        'nsg_id': 'int',
        'group': 'str',
        'ddr': 'Ec2DDR',
        'credentials': 'EC2NetscanPolicyCredential',
        'accessibility': 'str',
        'dead_operation': 'str',
        'ports': 'RestNetscanPorts'
    }

    attribute_map = {
        'creator': 'creator',
        'collector_group_name': 'collectorGroupName',
        'method': 'method',
        'collector_group': 'collectorGroup',
        'description': 'description',
        'next_start': 'nextStart',
        'duplicate': 'duplicate',
        'version': 'version',
        'collector': 'collector',
        'ignore_system_i_ps_duplicates': 'ignoreSystemIPsDuplicates',
        'schedule': 'schedule',
        'collector_description': 'collectorDescription',
        'name': 'name',
        'next_start_epoch': 'nextStartEpoch',
        'id': 'id',
        'nsg_id': 'nsgId',
        'group': 'group',
        'ddr': 'ddr',
        'credentials': 'credentials',
        'accessibility': 'accessibility',
        'dead_operation': 'deadOperation',
        'ports': 'ports'
    }

    def __init__(self, creator=None, collector_group_name=None, method=None, collector_group=None, description=None, next_start=None, duplicate=None, version=None, collector=None, ignore_system_i_ps_duplicates=None, schedule=None, collector_description=None, name=None, next_start_epoch=None, id=None, nsg_id=None, group=None, ddr=None, credentials=None, accessibility=None, dead_operation=None, ports=None):  # noqa: E501
        """Ec2Netscan - a model defined in Swagger"""  # noqa: E501

        self._creator = None
        self._collector_group_name = None
        self._method = None
        self._collector_group = None
        self._description = None
        self._next_start = None
        self._duplicate = None
        self._version = None
        self._collector = None
        self._ignore_system_i_ps_duplicates = None
        self._schedule = None
        self._collector_description = None
        self._name = None
        self._next_start_epoch = None
        self._id = None
        self._nsg_id = None
        self._group = None
        self._ddr = None
        self._credentials = None
        self._accessibility = None
        self._dead_operation = None
        self._ports = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        if collector_group_name is not None:
            self.collector_group_name = collector_group_name
        self.method = method
        if collector_group is not None:
            self.collector_group = collector_group
        if description is not None:
            self.description = description
        if next_start is not None:
            self.next_start = next_start
        self.duplicate = duplicate
        if version is not None:
            self.version = version
        if collector is not None:
            self.collector = collector
        if ignore_system_i_ps_duplicates is not None:
            self.ignore_system_i_ps_duplicates = ignore_system_i_ps_duplicates
        self.schedule = schedule
        if collector_description is not None:
            self.collector_description = collector_description
        self.name = name
        if next_start_epoch is not None:
            self.next_start_epoch = next_start_epoch
        if id is not None:
            self.id = id
        if nsg_id is not None:
            self.nsg_id = nsg_id
        if group is not None:
            self.group = group
        if ddr is not None:
            self.ddr = ddr
        self.credentials = credentials
        self.accessibility = accessibility
        if dead_operation is not None:
            self.dead_operation = dead_operation
        if ports is not None:
            self.ports = ports

    @property
    def creator(self):
        """Gets the creator of this Ec2Netscan.  # noqa: E501

        The user that created the policy  # noqa: E501

        :return: The creator of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Ec2Netscan.

        The user that created the policy  # noqa: E501

        :param creator: The creator of this Ec2Netscan.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def collector_group_name(self):
        """Gets the collector_group_name of this Ec2Netscan.  # noqa: E501

        The name of the group of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_group_name of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._collector_group_name

    @collector_group_name.setter
    def collector_group_name(self, collector_group_name):
        """Sets the collector_group_name of this Ec2Netscan.

        The name of the group of the Collector associated with this Netscan  # noqa: E501

        :param collector_group_name: The collector_group_name of this Ec2Netscan.  # noqa: E501
        :type: str
        """

        self._collector_group_name = collector_group_name

    @property
    def method(self):
        """Gets the method of this Ec2Netscan.  # noqa: E501

        The method that should be used to discover devices. Options are nmap (ICMP Ping), nec2 (EC2), enhancedScript and script  # noqa: E501

        :return: The method of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Ec2Netscan.

        The method that should be used to discover devices. Options are nmap (ICMP Ping), nec2 (EC2), enhancedScript and script  # noqa: E501

        :param method: The method of this Ec2Netscan.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def collector_group(self):
        """Gets the collector_group of this Ec2Netscan.  # noqa: E501

        The ID of the group of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_group of this Ec2Netscan.  # noqa: E501
        :rtype: int
        """
        return self._collector_group

    @collector_group.setter
    def collector_group(self, collector_group):
        """Sets the collector_group of this Ec2Netscan.

        The ID of the group of the Collector associated with this Netscan  # noqa: E501

        :param collector_group: The collector_group of this Ec2Netscan.  # noqa: E501
        :type: int
        """

        self._collector_group = collector_group

    @property
    def description(self):
        """Gets the description of this Ec2Netscan.  # noqa: E501

        The description of the Netscan Policy  # noqa: E501

        :return: The description of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Ec2Netscan.

        The description of the Netscan Policy  # noqa: E501

        :param description: The description of this Ec2Netscan.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def next_start(self):
        """Gets the next_start of this Ec2Netscan.  # noqa: E501

        The date and time of the next start time of the scan - displayed as manual if the scan does not run on a schedule  # noqa: E501

        :return: The next_start of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._next_start

    @next_start.setter
    def next_start(self, next_start):
        """Sets the next_start of this Ec2Netscan.

        The date and time of the next start time of the scan - displayed as manual if the scan does not run on a schedule  # noqa: E501

        :param next_start: The next_start of this Ec2Netscan.  # noqa: E501
        :type: str
        """

        self._next_start = next_start

    @property
    def duplicate(self):
        """Gets the duplicate of this Ec2Netscan.  # noqa: E501

        Information that determines how duplicate discovered devices should be handled  # noqa: E501

        :return: The duplicate of this Ec2Netscan.  # noqa: E501
        :rtype: ExcludeDuplicateIps
        """
        return self._duplicate

    @duplicate.setter
    def duplicate(self, duplicate):
        """Sets the duplicate of this Ec2Netscan.

        Information that determines how duplicate discovered devices should be handled  # noqa: E501

        :param duplicate: The duplicate of this Ec2Netscan.  # noqa: E501
        :type: ExcludeDuplicateIps
        """
        if duplicate is None:
            raise ValueError("Invalid value for `duplicate`, must not be `None`")  # noqa: E501

        self._duplicate = duplicate

    @property
    def version(self):
        """Gets the version of this Ec2Netscan.  # noqa: E501

        The Id of the device  # noqa: E501

        :return: The version of this Ec2Netscan.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Ec2Netscan.

        The Id of the device  # noqa: E501

        :param version: The version of this Ec2Netscan.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def collector(self):
        """Gets the collector of this Ec2Netscan.  # noqa: E501

        The ID of the Collector associated with this Netscan  # noqa: E501

        :return: The collector of this Ec2Netscan.  # noqa: E501
        :rtype: int
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """Sets the collector of this Ec2Netscan.

        The ID of the Collector associated with this Netscan  # noqa: E501

        :param collector: The collector of this Ec2Netscan.  # noqa: E501
        :type: int
        """

        self._collector = collector

    @property
    def ignore_system_i_ps_duplicates(self):
        """Gets the ignore_system_i_ps_duplicates of this Ec2Netscan.  # noqa: E501

        Ignore system.ips when checking for duplicate resources  # noqa: E501

        :return: The ignore_system_i_ps_duplicates of this Ec2Netscan.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_system_i_ps_duplicates

    @ignore_system_i_ps_duplicates.setter
    def ignore_system_i_ps_duplicates(self, ignore_system_i_ps_duplicates):
        """Sets the ignore_system_i_ps_duplicates of this Ec2Netscan.

        Ignore system.ips when checking for duplicate resources  # noqa: E501

        :param ignore_system_i_ps_duplicates: The ignore_system_i_ps_duplicates of this Ec2Netscan.  # noqa: E501
        :type: bool
        """

        self._ignore_system_i_ps_duplicates = ignore_system_i_ps_duplicates

    @property
    def schedule(self):
        """Gets the schedule of this Ec2Netscan.  # noqa: E501

        Information related to the recurring execution schedule for the Netscan Policy  # noqa: E501

        :return: The schedule of this Ec2Netscan.  # noqa: E501
        :rtype: RestSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this Ec2Netscan.

        Information related to the recurring execution schedule for the Netscan Policy  # noqa: E501

        :param schedule: The schedule of this Ec2Netscan.  # noqa: E501
        :type: RestSchedule
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def collector_description(self):
        """Gets the collector_description of this Ec2Netscan.  # noqa: E501

        The description of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_description of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._collector_description

    @collector_description.setter
    def collector_description(self, collector_description):
        """Sets the collector_description of this Ec2Netscan.

        The description of the Collector associated with this Netscan  # noqa: E501

        :param collector_description: The collector_description of this Ec2Netscan.  # noqa: E501
        :type: str
        """

        self._collector_description = collector_description

    @property
    def name(self):
        """Gets the name of this Ec2Netscan.  # noqa: E501

        The name of the Netscan Policy  # noqa: E501

        :return: The name of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Ec2Netscan.

        The name of the Netscan Policy  # noqa: E501

        :param name: The name of this Ec2Netscan.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def next_start_epoch(self):
        """Gets the next_start_epoch of this Ec2Netscan.  # noqa: E501

        The epoch of the next start time of the scan - displayed as 0 if the scan does not run on a schedule  # noqa: E501

        :return: The next_start_epoch of this Ec2Netscan.  # noqa: E501
        :rtype: int
        """
        return self._next_start_epoch

    @next_start_epoch.setter
    def next_start_epoch(self, next_start_epoch):
        """Sets the next_start_epoch of this Ec2Netscan.

        The epoch of the next start time of the scan - displayed as 0 if the scan does not run on a schedule  # noqa: E501

        :param next_start_epoch: The next_start_epoch of this Ec2Netscan.  # noqa: E501
        :type: int
        """

        self._next_start_epoch = next_start_epoch

    @property
    def id(self):
        """Gets the id of this Ec2Netscan.  # noqa: E501

        The ID of the Netscan Policy  # noqa: E501

        :return: The id of this Ec2Netscan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Ec2Netscan.

        The ID of the Netscan Policy  # noqa: E501

        :param id: The id of this Ec2Netscan.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def nsg_id(self):
        """Gets the nsg_id of this Ec2Netscan.  # noqa: E501

        The ID of the group the policy belongs to  # noqa: E501

        :return: The nsg_id of this Ec2Netscan.  # noqa: E501
        :rtype: int
        """
        return self._nsg_id

    @nsg_id.setter
    def nsg_id(self, nsg_id):
        """Sets the nsg_id of this Ec2Netscan.

        The ID of the group the policy belongs to  # noqa: E501

        :param nsg_id: The nsg_id of this Ec2Netscan.  # noqa: E501
        :type: int
        """

        self._nsg_id = nsg_id

    @property
    def group(self):
        """Gets the group of this Ec2Netscan.  # noqa: E501

        The group the Netscan policy should belong to  # noqa: E501

        :return: The group of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Ec2Netscan.

        The group the Netscan policy should belong to  # noqa: E501

        :param group: The group of this Ec2Netscan.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def ddr(self):
        """Gets the ddr of this Ec2Netscan.  # noqa: E501


        :return: The ddr of this Ec2Netscan.  # noqa: E501
        :rtype: Ec2DDR
        """
        return self._ddr

    @ddr.setter
    def ddr(self, ddr):
        """Sets the ddr of this Ec2Netscan.


        :param ddr: The ddr of this Ec2Netscan.  # noqa: E501
        :type: Ec2DDR
        """

        self._ddr = ddr

    @property
    def credentials(self):
        """Gets the credentials of this Ec2Netscan.  # noqa: E501

        The credentials to be used for the scan  # noqa: E501

        :return: The credentials of this Ec2Netscan.  # noqa: E501
        :rtype: EC2NetscanPolicyCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Ec2Netscan.

        The credentials to be used for the scan  # noqa: E501

        :param credentials: The credentials of this Ec2Netscan.  # noqa: E501
        :type: EC2NetscanPolicyCredential
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def accessibility(self):
        """Gets the accessibility of this Ec2Netscan.  # noqa: E501

        Which IP the EC2 instance should be monitored with for nec2 scans: private or public  # noqa: E501

        :return: The accessibility of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility):
        """Sets the accessibility of this Ec2Netscan.

        Which IP the EC2 instance should be monitored with for nec2 scans: private or public  # noqa: E501

        :param accessibility: The accessibility of this Ec2Netscan.  # noqa: E501
        :type: str
        """
        if accessibility is None:
            raise ValueError("Invalid value for `accessibility`, must not be `None`")  # noqa: E501

        self._accessibility = accessibility

    @property
    def dead_operation(self):
        """Gets the dead_operation of this Ec2Netscan.  # noqa: E501

        How dead EC2 instances should be handled for nec2 scans. Must be Manually  # noqa: E501

        :return: The dead_operation of this Ec2Netscan.  # noqa: E501
        :rtype: str
        """
        return self._dead_operation

    @dead_operation.setter
    def dead_operation(self, dead_operation):
        """Sets the dead_operation of this Ec2Netscan.

        How dead EC2 instances should be handled for nec2 scans. Must be Manually  # noqa: E501

        :param dead_operation: The dead_operation of this Ec2Netscan.  # noqa: E501
        :type: str
        """

        self._dead_operation = dead_operation

    @property
    def ports(self):
        """Gets the ports of this Ec2Netscan.  # noqa: E501


        :return: The ports of this Ec2Netscan.  # noqa: E501
        :rtype: RestNetscanPorts
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this Ec2Netscan.


        :param ports: The ports of this Ec2Netscan.  # noqa: E501
        :type: RestNetscanPorts
        """

        self._ports = ports

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
        if issubclass(Ec2Netscan, dict):
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
        if not isinstance(other, Ec2Netscan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
