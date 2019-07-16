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

from logicmonitor_sdk.models.aws_account_test_result import AwsAccountTestResult  # noqa: F401,E501
from logicmonitor_sdk.models.azure_account_test_result import AzureAccountTestResult  # noqa: F401,E501
from logicmonitor_sdk.models.device_group_data import DeviceGroupData  # noqa: F401,E501
from logicmonitor_sdk.models.gcp_account_test_result import GcpAccountTestResult  # noqa: F401,E501
from logicmonitor_sdk.models.name_and_value import NameAndValue  # noqa: F401,E501


class DeviceGroup(object):
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
        'applies_to': 'str',
        'aws_regions_info': 'str',
        'aws_test_result': 'AwsAccountTestResult',
        'aws_test_result_code': 'int',
        'azure_regions_info': 'str',
        'azure_test_result': 'AzureAccountTestResult',
        'azure_test_result_code': 'int',
        'created_on': 'int',
        'custom_properties': 'list[NameAndValue]',
        'default_collector_description': 'str',
        'default_collector_id': 'int',
        'description': 'str',
        'disable_alerting': 'bool',
        'effective_alert_enabled': 'bool',
        'enable_netflow': 'object',
        'extra': 'object',
        'full_path': 'str',
        'gcp_regions_info': 'str',
        'gcp_test_result': 'GcpAccountTestResult',
        'gcp_test_result_code': 'int',
        'group_status': 'str',
        'group_type': 'str',
        'has_netflow_enabled_devices': 'bool',
        'id': 'int',
        'name': 'str',
        'num_of_aws_devices': 'int',
        'num_of_azure_devices': 'int',
        'num_of_direct_devices': 'int',
        'num_of_direct_sub_groups': 'int',
        'num_of_gcp_devices': 'int',
        'num_of_hosts': 'int',
        'parent_id': 'int',
        'sub_groups': 'list[DeviceGroupData]',
        'user_permission': 'str'
    }

    attribute_map = {
        'applies_to': 'appliesTo',
        'aws_regions_info': 'awsRegionsInfo',
        'aws_test_result': 'awsTestResult',
        'aws_test_result_code': 'awsTestResultCode',
        'azure_regions_info': 'azureRegionsInfo',
        'azure_test_result': 'azureTestResult',
        'azure_test_result_code': 'azureTestResultCode',
        'created_on': 'createdOn',
        'custom_properties': 'customProperties',
        'default_collector_description': 'defaultCollectorDescription',
        'default_collector_id': 'defaultCollectorId',
        'description': 'description',
        'disable_alerting': 'disableAlerting',
        'effective_alert_enabled': 'effectiveAlertEnabled',
        'enable_netflow': 'enableNetflow',
        'extra': 'extra',
        'full_path': 'fullPath',
        'gcp_regions_info': 'gcpRegionsInfo',
        'gcp_test_result': 'gcpTestResult',
        'gcp_test_result_code': 'gcpTestResultCode',
        'group_status': 'groupStatus',
        'group_type': 'groupType',
        'has_netflow_enabled_devices': 'hasNetflowEnabledDevices',
        'id': 'id',
        'name': 'name',
        'num_of_aws_devices': 'numOfAWSDevices',
        'num_of_azure_devices': 'numOfAzureDevices',
        'num_of_direct_devices': 'numOfDirectDevices',
        'num_of_direct_sub_groups': 'numOfDirectSubGroups',
        'num_of_gcp_devices': 'numOfGcpDevices',
        'num_of_hosts': 'numOfHosts',
        'parent_id': 'parentId',
        'sub_groups': 'subGroups',
        'user_permission': 'userPermission'
    }

    def __init__(self, applies_to=None, aws_regions_info=None, aws_test_result=None, aws_test_result_code=None, azure_regions_info=None, azure_test_result=None, azure_test_result_code=None, created_on=None, custom_properties=None, default_collector_description=None, default_collector_id=None, description=None, disable_alerting=None, effective_alert_enabled=None, enable_netflow=None, extra=None, full_path=None, gcp_regions_info=None, gcp_test_result=None, gcp_test_result_code=None, group_status=None, group_type=None, has_netflow_enabled_devices=None, id=None, name=None, num_of_aws_devices=None, num_of_azure_devices=None, num_of_direct_devices=None, num_of_direct_sub_groups=None, num_of_gcp_devices=None, num_of_hosts=None, parent_id=None, sub_groups=None, user_permission=None):  # noqa: E501
        """DeviceGroup - a model defined in Swagger"""  # noqa: E501

        self._applies_to = None
        self._aws_regions_info = None
        self._aws_test_result = None
        self._aws_test_result_code = None
        self._azure_regions_info = None
        self._azure_test_result = None
        self._azure_test_result_code = None
        self._created_on = None
        self._custom_properties = None
        self._default_collector_description = None
        self._default_collector_id = None
        self._description = None
        self._disable_alerting = None
        self._effective_alert_enabled = None
        self._enable_netflow = None
        self._extra = None
        self._full_path = None
        self._gcp_regions_info = None
        self._gcp_test_result = None
        self._gcp_test_result_code = None
        self._group_status = None
        self._group_type = None
        self._has_netflow_enabled_devices = None
        self._id = None
        self._name = None
        self._num_of_aws_devices = None
        self._num_of_azure_devices = None
        self._num_of_direct_devices = None
        self._num_of_direct_sub_groups = None
        self._num_of_gcp_devices = None
        self._num_of_hosts = None
        self._parent_id = None
        self._sub_groups = None
        self._user_permission = None
        self.discriminator = None

        if applies_to is not None:
            self.applies_to = applies_to
        if aws_regions_info is not None:
            self.aws_regions_info = aws_regions_info
        if aws_test_result is not None:
            self.aws_test_result = aws_test_result
        if aws_test_result_code is not None:
            self.aws_test_result_code = aws_test_result_code
        if azure_regions_info is not None:
            self.azure_regions_info = azure_regions_info
        if azure_test_result is not None:
            self.azure_test_result = azure_test_result
        if azure_test_result_code is not None:
            self.azure_test_result_code = azure_test_result_code
        if created_on is not None:
            self.created_on = created_on
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if default_collector_description is not None:
            self.default_collector_description = default_collector_description
        if default_collector_id is not None:
            self.default_collector_id = default_collector_id
        if description is not None:
            self.description = description
        if disable_alerting is not None:
            self.disable_alerting = disable_alerting
        if effective_alert_enabled is not None:
            self.effective_alert_enabled = effective_alert_enabled
        if enable_netflow is not None:
            self.enable_netflow = enable_netflow
        if extra is not None:
            self.extra = extra
        if full_path is not None:
            self.full_path = full_path
        if gcp_regions_info is not None:
            self.gcp_regions_info = gcp_regions_info
        if gcp_test_result is not None:
            self.gcp_test_result = gcp_test_result
        if gcp_test_result_code is not None:
            self.gcp_test_result_code = gcp_test_result_code
        if group_status is not None:
            self.group_status = group_status
        if group_type is not None:
            self.group_type = group_type
        if has_netflow_enabled_devices is not None:
            self.has_netflow_enabled_devices = has_netflow_enabled_devices
        if id is not None:
            self.id = id
        self.name = name
        if num_of_aws_devices is not None:
            self.num_of_aws_devices = num_of_aws_devices
        if num_of_azure_devices is not None:
            self.num_of_azure_devices = num_of_azure_devices
        if num_of_direct_devices is not None:
            self.num_of_direct_devices = num_of_direct_devices
        if num_of_direct_sub_groups is not None:
            self.num_of_direct_sub_groups = num_of_direct_sub_groups
        if num_of_gcp_devices is not None:
            self.num_of_gcp_devices = num_of_gcp_devices
        if num_of_hosts is not None:
            self.num_of_hosts = num_of_hosts
        if parent_id is not None:
            self.parent_id = parent_id
        if sub_groups is not None:
            self.sub_groups = sub_groups
        if user_permission is not None:
            self.user_permission = user_permission

    @property
    def applies_to(self):
        """Gets the applies_to of this DeviceGroup.  # noqa: E501

        The Applies to custom query for this group (only for dynamic groups)  # noqa: E501

        :return: The applies_to of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this DeviceGroup.

        The Applies to custom query for this group (only for dynamic groups)  # noqa: E501

        :param applies_to: The applies_to of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._applies_to = applies_to

    @property
    def aws_regions_info(self):
        """Gets the aws_regions_info of this DeviceGroup.  # noqa: E501

        The number of instances in each AWS region (only applies to AWS groups)  # noqa: E501

        :return: The aws_regions_info of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._aws_regions_info

    @aws_regions_info.setter
    def aws_regions_info(self, aws_regions_info):
        """Sets the aws_regions_info of this DeviceGroup.

        The number of instances in each AWS region (only applies to AWS groups)  # noqa: E501

        :param aws_regions_info: The aws_regions_info of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._aws_regions_info = aws_regions_info

    @property
    def aws_test_result(self):
        """Gets the aws_test_result of this DeviceGroup.  # noqa: E501

        The String result returned by the transaction that tests the AWS credentials associated with the AWS group  # noqa: E501

        :return: The aws_test_result of this DeviceGroup.  # noqa: E501
        :rtype: AwsAccountTestResult
        """
        return self._aws_test_result

    @aws_test_result.setter
    def aws_test_result(self, aws_test_result):
        """Sets the aws_test_result of this DeviceGroup.

        The String result returned by the transaction that tests the AWS credentials associated with the AWS group  # noqa: E501

        :param aws_test_result: The aws_test_result of this DeviceGroup.  # noqa: E501
        :type: AwsAccountTestResult
        """

        self._aws_test_result = aws_test_result

    @property
    def aws_test_result_code(self):
        """Gets the aws_test_result_code of this DeviceGroup.  # noqa: E501

        The Status code result returned by the transaction that tests the AWS credentials associated with the AWS group  # noqa: E501

        :return: The aws_test_result_code of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._aws_test_result_code

    @aws_test_result_code.setter
    def aws_test_result_code(self, aws_test_result_code):
        """Sets the aws_test_result_code of this DeviceGroup.

        The Status code result returned by the transaction that tests the AWS credentials associated with the AWS group  # noqa: E501

        :param aws_test_result_code: The aws_test_result_code of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._aws_test_result_code = aws_test_result_code

    @property
    def azure_regions_info(self):
        """Gets the azure_regions_info of this DeviceGroup.  # noqa: E501

        The number of instances in each Azure region (only applies to Azure groups)  # noqa: E501

        :return: The azure_regions_info of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._azure_regions_info

    @azure_regions_info.setter
    def azure_regions_info(self, azure_regions_info):
        """Sets the azure_regions_info of this DeviceGroup.

        The number of instances in each Azure region (only applies to Azure groups)  # noqa: E501

        :param azure_regions_info: The azure_regions_info of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._azure_regions_info = azure_regions_info

    @property
    def azure_test_result(self):
        """Gets the azure_test_result of this DeviceGroup.  # noqa: E501

        The String result returned by the transaction that tests the Azure credentials associated with the Azure group  # noqa: E501

        :return: The azure_test_result of this DeviceGroup.  # noqa: E501
        :rtype: AzureAccountTestResult
        """
        return self._azure_test_result

    @azure_test_result.setter
    def azure_test_result(self, azure_test_result):
        """Sets the azure_test_result of this DeviceGroup.

        The String result returned by the transaction that tests the Azure credentials associated with the Azure group  # noqa: E501

        :param azure_test_result: The azure_test_result of this DeviceGroup.  # noqa: E501
        :type: AzureAccountTestResult
        """

        self._azure_test_result = azure_test_result

    @property
    def azure_test_result_code(self):
        """Gets the azure_test_result_code of this DeviceGroup.  # noqa: E501

        The Status code result returned by the transaction that tests the Azure credentials associated with the Azure group  # noqa: E501

        :return: The azure_test_result_code of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._azure_test_result_code

    @azure_test_result_code.setter
    def azure_test_result_code(self, azure_test_result_code):
        """Sets the azure_test_result_code of this DeviceGroup.

        The Status code result returned by the transaction that tests the Azure credentials associated with the Azure group  # noqa: E501

        :param azure_test_result_code: The azure_test_result_code of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._azure_test_result_code = azure_test_result_code

    @property
    def created_on(self):
        """Gets the created_on of this DeviceGroup.  # noqa: E501

        The time, in epoch seconds format, that the device group was created  # noqa: E501

        :return: The created_on of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeviceGroup.

        The time, in epoch seconds format, that the device group was created  # noqa: E501

        :param created_on: The created_on of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def custom_properties(self):
        """Gets the custom_properties of this DeviceGroup.  # noqa: E501

        The properties associated with this device group  # noqa: E501

        :return: The custom_properties of this DeviceGroup.  # noqa: E501
        :rtype: list[NameAndValue]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this DeviceGroup.

        The properties associated with this device group  # noqa: E501

        :param custom_properties: The custom_properties of this DeviceGroup.  # noqa: E501
        :type: list[NameAndValue]
        """

        self._custom_properties = custom_properties

    @property
    def default_collector_description(self):
        """Gets the default_collector_description of this DeviceGroup.  # noqa: E501

        The description of the default collector assigned to the device group  # noqa: E501

        :return: The default_collector_description of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._default_collector_description

    @default_collector_description.setter
    def default_collector_description(self, default_collector_description):
        """Sets the default_collector_description of this DeviceGroup.

        The description of the default collector assigned to the device group  # noqa: E501

        :param default_collector_description: The default_collector_description of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._default_collector_description = default_collector_description

    @property
    def default_collector_id(self):
        """Gets the default_collector_id of this DeviceGroup.  # noqa: E501

        The Id of the default collector assigned to the device group  # noqa: E501

        :return: The default_collector_id of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._default_collector_id

    @default_collector_id.setter
    def default_collector_id(self, default_collector_id):
        """Sets the default_collector_id of this DeviceGroup.

        The Id of the default collector assigned to the device group  # noqa: E501

        :param default_collector_id: The default_collector_id of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._default_collector_id = default_collector_id

    @property
    def description(self):
        """Gets the description of this DeviceGroup.  # noqa: E501

        The description of the device group  # noqa: E501

        :return: The description of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceGroup.

        The description of the device group  # noqa: E501

        :param description: The description of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disable_alerting(self):
        """Gets the disable_alerting of this DeviceGroup.  # noqa: E501

        Indicates whether alerting is disabled (true) or enabled (false) for this device group  # noqa: E501

        :return: The disable_alerting of this DeviceGroup.  # noqa: E501
        :rtype: bool
        """
        return self._disable_alerting

    @disable_alerting.setter
    def disable_alerting(self, disable_alerting):
        """Sets the disable_alerting of this DeviceGroup.

        Indicates whether alerting is disabled (true) or enabled (false) for this device group  # noqa: E501

        :param disable_alerting: The disable_alerting of this DeviceGroup.  # noqa: E501
        :type: bool
        """

        self._disable_alerting = disable_alerting

    @property
    def effective_alert_enabled(self):
        """Gets the effective_alert_enabled of this DeviceGroup.  # noqa: E501

        Whether or not alerting is effectively disabled for this device group (alerting may be disabled at a higher level, e.g. parent group)  # noqa: E501

        :return: The effective_alert_enabled of this DeviceGroup.  # noqa: E501
        :rtype: bool
        """
        return self._effective_alert_enabled

    @effective_alert_enabled.setter
    def effective_alert_enabled(self, effective_alert_enabled):
        """Sets the effective_alert_enabled of this DeviceGroup.

        Whether or not alerting is effectively disabled for this device group (alerting may be disabled at a higher level, e.g. parent group)  # noqa: E501

        :param effective_alert_enabled: The effective_alert_enabled of this DeviceGroup.  # noqa: E501
        :type: bool
        """

        self._effective_alert_enabled = effective_alert_enabled

    @property
    def enable_netflow(self):
        """Gets the enable_netflow of this DeviceGroup.  # noqa: E501

        Indicates whether Netflow is enabled (true) or disabled (false) for the device group, the default value is true  # noqa: E501

        :return: The enable_netflow of this DeviceGroup.  # noqa: E501
        :rtype: object
        """
        return self._enable_netflow

    @enable_netflow.setter
    def enable_netflow(self, enable_netflow):
        """Sets the enable_netflow of this DeviceGroup.

        Indicates whether Netflow is enabled (true) or disabled (false) for the device group, the default value is true  # noqa: E501

        :param enable_netflow: The enable_netflow of this DeviceGroup.  # noqa: E501
        :type: object
        """

        self._enable_netflow = enable_netflow

    @property
    def extra(self):
        """Gets the extra of this DeviceGroup.  # noqa: E501

        The extra setting for cloud group  # noqa: E501

        :return: The extra of this DeviceGroup.  # noqa: E501
        :rtype: object
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this DeviceGroup.

        The extra setting for cloud group  # noqa: E501

        :param extra: The extra of this DeviceGroup.  # noqa: E501
        :type: object
        """

        self._extra = extra

    @property
    def full_path(self):
        """Gets the full_path of this DeviceGroup.  # noqa: E501

        The full path of the device group (i.e. if the group 'Dev' is under a parent group named 'Production', the fullPath would be 'Production/Dev'  # noqa: E501

        :return: The full_path of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        """Sets the full_path of this DeviceGroup.

        The full path of the device group (i.e. if the group 'Dev' is under a parent group named 'Production', the fullPath would be 'Production/Dev'  # noqa: E501

        :param full_path: The full_path of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._full_path = full_path

    @property
    def gcp_regions_info(self):
        """Gets the gcp_regions_info of this DeviceGroup.  # noqa: E501


        :return: The gcp_regions_info of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._gcp_regions_info

    @gcp_regions_info.setter
    def gcp_regions_info(self, gcp_regions_info):
        """Sets the gcp_regions_info of this DeviceGroup.


        :param gcp_regions_info: The gcp_regions_info of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._gcp_regions_info = gcp_regions_info

    @property
    def gcp_test_result(self):
        """Gets the gcp_test_result of this DeviceGroup.  # noqa: E501

        The result returned by the transaction that tests the GCP credentials associated with the GCP group  # noqa: E501

        :return: The gcp_test_result of this DeviceGroup.  # noqa: E501
        :rtype: GcpAccountTestResult
        """
        return self._gcp_test_result

    @gcp_test_result.setter
    def gcp_test_result(self, gcp_test_result):
        """Sets the gcp_test_result of this DeviceGroup.

        The result returned by the transaction that tests the GCP credentials associated with the GCP group  # noqa: E501

        :param gcp_test_result: The gcp_test_result of this DeviceGroup.  # noqa: E501
        :type: GcpAccountTestResult
        """

        self._gcp_test_result = gcp_test_result

    @property
    def gcp_test_result_code(self):
        """Gets the gcp_test_result_code of this DeviceGroup.  # noqa: E501

        The Status code result returned by the transaction that tests the GCP credentials associated with the GCP group  # noqa: E501

        :return: The gcp_test_result_code of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._gcp_test_result_code

    @gcp_test_result_code.setter
    def gcp_test_result_code(self, gcp_test_result_code):
        """Sets the gcp_test_result_code of this DeviceGroup.

        The Status code result returned by the transaction that tests the GCP credentials associated with the GCP group  # noqa: E501

        :param gcp_test_result_code: The gcp_test_result_code of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._gcp_test_result_code = gcp_test_result_code

    @property
    def group_status(self):
        """Gets the group_status of this DeviceGroup.  # noqa: E501

        normal | dead  The status of this device group, where possible statuses are normal and dead. A group with a status of dead may indicate that one or more devices are dead within the group  # noqa: E501

        :return: The group_status of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_status

    @group_status.setter
    def group_status(self, group_status):
        """Sets the group_status of this DeviceGroup.

        normal | dead  The status of this device group, where possible statuses are normal and dead. A group with a status of dead may indicate that one or more devices are dead within the group  # noqa: E501

        :param group_status: The group_status of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._group_status = group_status

    @property
    def group_type(self):
        """Gets the group_type of this DeviceGroup.  # noqa: E501

        The type of device group: normal and dynamic device groups will have groupType=Normal, and AWS groups will have a groupType value of AWS/SERVICE (e.g. AWS/S3)  # noqa: E501

        :return: The group_type of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this DeviceGroup.

        The type of device group: normal and dynamic device groups will have groupType=Normal, and AWS groups will have a groupType value of AWS/SERVICE (e.g. AWS/S3)  # noqa: E501

        :param group_type: The group_type of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._group_type = group_type

    @property
    def has_netflow_enabled_devices(self):
        """Gets the has_netflow_enabled_devices of this DeviceGroup.  # noqa: E501

        Whether if any Netflow enabled devices in this device group  # noqa: E501

        :return: The has_netflow_enabled_devices of this DeviceGroup.  # noqa: E501
        :rtype: bool
        """
        return self._has_netflow_enabled_devices

    @has_netflow_enabled_devices.setter
    def has_netflow_enabled_devices(self, has_netflow_enabled_devices):
        """Sets the has_netflow_enabled_devices of this DeviceGroup.

        Whether if any Netflow enabled devices in this device group  # noqa: E501

        :param has_netflow_enabled_devices: The has_netflow_enabled_devices of this DeviceGroup.  # noqa: E501
        :type: bool
        """

        self._has_netflow_enabled_devices = has_netflow_enabled_devices

    @property
    def id(self):
        """Gets the id of this DeviceGroup.  # noqa: E501

        The id of the device group  # noqa: E501

        :return: The id of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceGroup.

        The id of the device group  # noqa: E501

        :param id: The id of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeviceGroup.  # noqa: E501

        The name of the device group  # noqa: E501

        :return: The name of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceGroup.

        The name of the device group  # noqa: E501

        :param name: The name of this DeviceGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def num_of_aws_devices(self):
        """Gets the num_of_aws_devices of this DeviceGroup.  # noqa: E501

        The number of AWS devices that belong to this device group (includes AWS devices in sub groups)  # noqa: E501

        :return: The num_of_aws_devices of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_aws_devices

    @num_of_aws_devices.setter
    def num_of_aws_devices(self, num_of_aws_devices):
        """Sets the num_of_aws_devices of this DeviceGroup.

        The number of AWS devices that belong to this device group (includes AWS devices in sub groups)  # noqa: E501

        :param num_of_aws_devices: The num_of_aws_devices of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._num_of_aws_devices = num_of_aws_devices

    @property
    def num_of_azure_devices(self):
        """Gets the num_of_azure_devices of this DeviceGroup.  # noqa: E501

        The number of Azure devices that belong to this device group (includes Azure devices in sub groups)  # noqa: E501

        :return: The num_of_azure_devices of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_azure_devices

    @num_of_azure_devices.setter
    def num_of_azure_devices(self, num_of_azure_devices):
        """Sets the num_of_azure_devices of this DeviceGroup.

        The number of Azure devices that belong to this device group (includes Azure devices in sub groups)  # noqa: E501

        :param num_of_azure_devices: The num_of_azure_devices of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._num_of_azure_devices = num_of_azure_devices

    @property
    def num_of_direct_devices(self):
        """Gets the num_of_direct_devices of this DeviceGroup.  # noqa: E501

        The number of AWS and normal devices that belong only to this device group (doesn't include devices in sub-groups)  # noqa: E501

        :return: The num_of_direct_devices of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_direct_devices

    @num_of_direct_devices.setter
    def num_of_direct_devices(self, num_of_direct_devices):
        """Sets the num_of_direct_devices of this DeviceGroup.

        The number of AWS and normal devices that belong only to this device group (doesn't include devices in sub-groups)  # noqa: E501

        :param num_of_direct_devices: The num_of_direct_devices of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._num_of_direct_devices = num_of_direct_devices

    @property
    def num_of_direct_sub_groups(self):
        """Gets the num_of_direct_sub_groups of this DeviceGroup.  # noqa: E501

        The number of sub-groups that belong only to this device group (doesn't include groups under sub-groups)  # noqa: E501

        :return: The num_of_direct_sub_groups of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_direct_sub_groups

    @num_of_direct_sub_groups.setter
    def num_of_direct_sub_groups(self, num_of_direct_sub_groups):
        """Sets the num_of_direct_sub_groups of this DeviceGroup.

        The number of sub-groups that belong only to this device group (doesn't include groups under sub-groups)  # noqa: E501

        :param num_of_direct_sub_groups: The num_of_direct_sub_groups of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._num_of_direct_sub_groups = num_of_direct_sub_groups

    @property
    def num_of_gcp_devices(self):
        """Gets the num_of_gcp_devices of this DeviceGroup.  # noqa: E501


        :return: The num_of_gcp_devices of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_gcp_devices

    @num_of_gcp_devices.setter
    def num_of_gcp_devices(self, num_of_gcp_devices):
        """Sets the num_of_gcp_devices of this DeviceGroup.


        :param num_of_gcp_devices: The num_of_gcp_devices of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._num_of_gcp_devices = num_of_gcp_devices

    @property
    def num_of_hosts(self):
        """Gets the num_of_hosts of this DeviceGroup.  # noqa: E501

        The number of total devices, including both AWS and normal devices, that belong to this device group (includes normal devices in sub groups)  # noqa: E501

        :return: The num_of_hosts of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._num_of_hosts

    @num_of_hosts.setter
    def num_of_hosts(self, num_of_hosts):
        """Sets the num_of_hosts of this DeviceGroup.

        The number of total devices, including both AWS and normal devices, that belong to this device group (includes normal devices in sub groups)  # noqa: E501

        :param num_of_hosts: The num_of_hosts of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._num_of_hosts = num_of_hosts

    @property
    def parent_id(self):
        """Gets the parent_id of this DeviceGroup.  # noqa: E501

        The id of the parent group for this device group (the root device group has an Id of 1)  # noqa: E501

        :return: The parent_id of this DeviceGroup.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this DeviceGroup.

        The id of the parent group for this device group (the root device group has an Id of 1)  # noqa: E501

        :param parent_id: The parent_id of this DeviceGroup.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def sub_groups(self):
        """Gets the sub_groups of this DeviceGroup.  # noqa: E501

        The child device groups within this device group  # noqa: E501

        :return: The sub_groups of this DeviceGroup.  # noqa: E501
        :rtype: list[DeviceGroupData]
        """
        return self._sub_groups

    @sub_groups.setter
    def sub_groups(self, sub_groups):
        """Sets the sub_groups of this DeviceGroup.

        The child device groups within this device group  # noqa: E501

        :param sub_groups: The sub_groups of this DeviceGroup.  # noqa: E501
        :type: list[DeviceGroupData]
        """

        self._sub_groups = sub_groups

    @property
    def user_permission(self):
        """Gets the user_permission of this DeviceGroup.  # noqa: E501

        The permissions for the device group that are granted to the user that made this API request  # noqa: E501

        :return: The user_permission of this DeviceGroup.  # noqa: E501
        :rtype: str
        """
        return self._user_permission

    @user_permission.setter
    def user_permission(self, user_permission):
        """Sets the user_permission of this DeviceGroup.

        The permissions for the device group that are granted to the user that made this API request  # noqa: E501

        :param user_permission: The user_permission of this DeviceGroup.  # noqa: E501
        :type: str
        """

        self._user_permission = user_permission

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
        if issubclass(DeviceGroup, dict):
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
        if not isinstance(other, DeviceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
