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

from logicmonitor_sdk.models.auto_discovery_method import AutoDiscoveryMethod  # noqa: F401,E501


class CloudWatchAutoDiscoveryMethod(AutoDiscoveryMethod):
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
        'cluster_dimension': 'str',
        'period': 'str',
        'metric_name': 'str',
        'node_dimension': 'str',
        'namespace': 'str',
        'cluster_dimension_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cluster_dimension': 'clusterDimension',
        'period': 'period',
        'metric_name': 'metricName',
        'node_dimension': 'nodeDimension',
        'namespace': 'namespace',
        'cluster_dimension_value': 'clusterDimensionValue'
    }

    def __init__(self, name=None, cluster_dimension=None, period=None, metric_name=None, node_dimension=None, namespace=None, cluster_dimension_value=None):  # noqa: E501
        """CloudWatchAutoDiscoveryMethod - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._cluster_dimension = None
        self._period = None
        self._metric_name = None
        self._node_dimension = None
        self._namespace = None
        self._cluster_dimension_value = None
        self.discriminator = None

        self.name = name
        self.cluster_dimension = cluster_dimension
        if period is not None:
            self.period = period
        if metric_name is not None:
            self.metric_name = metric_name
        self.node_dimension = node_dimension
        self.namespace = namespace
        if cluster_dimension_value is not None:
            self.cluster_dimension_value = cluster_dimension_value

    @property
    def name(self):
        """Gets the name of this CloudWatchAutoDiscoveryMethod.  # noqa: E501

        The auto discovery method name values can be : ad_cim|ad_cloudwatch|ad_collector|ad_dummy|ad_ec2|ad_esx|ad_http|ad_ipmi|ad_jdbc|ad_jmx|ad_netapp|ad_pdh|ad_port|ad_script|ad_snmp|ad_wmi|ad_xen|ad_azurerediscache|ad_awsserviceregion|ad_awsec2reservedinstance|ad_awsec2reservedinstancecoverage|ad_awsecsservice|ad_awsec2scheduledevents|ad_azureserviceregion|ad_azuresubscription|ad_azurebackupjob|ad_azuresdk|ad_azurewebjob|ad_awsbillingreport|ad_awselasticache|ad_awsredshift|ad_azurebilling|ad_awslbtargetgroups|ad_gcpappengine|ad_gcpbilling|ad_awsvpntunnel|ad_gcpvpntunnel|ad_awsglobalwebacl|ad_gcplbbackendservice|ad_gcppubsubsubscription|ad_gcppubsubsnapshot|ad_azurereplicationjob|ad_azureexpressroutecircuitpeering|ad_awsapigatewaystage|ad_azureautomationaccountcertificate|ad_azurevngconnection|ad_azurewebappinstance|ad_azureappserviceenvironmentmultirolepool|ad_openmetrics|ad_awsmediaconnectoutput|ad_awsmediaconnectsource|ad_awswebaclwafv2|ad_saaso365sharepointsite|ad_awscognitoidentityproviders|ad_azureeabilling|ad_saaszoomplanusage|ad_saasstatus|ad_azuresynapse|ad_saasairbrake|ad_syntheticsselenium|ad_azurevirtualdesktopsessionhosts|ad_saaso365subscribedsku|ad_azuredimension|ad_azurecostmanagementdimensions|ad_saaso365servicehealth|ad_saaso365mailbox|ad_azurenetappvolumes|ad_azureloganalyticsworkspaces|ad_saaszoomstatus|ad_saassalesforcelicense|ad_saaszoomroom|ad_saaswebexlicenseusage|ad_azureloganalyticsreplicationjob|ad_paasjsonpath  # noqa: E501

        :return: The name of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudWatchAutoDiscoveryMethod.

        The auto discovery method name values can be : ad_cim|ad_cloudwatch|ad_collector|ad_dummy|ad_ec2|ad_esx|ad_http|ad_ipmi|ad_jdbc|ad_jmx|ad_netapp|ad_pdh|ad_port|ad_script|ad_snmp|ad_wmi|ad_xen|ad_azurerediscache|ad_awsserviceregion|ad_awsec2reservedinstance|ad_awsec2reservedinstancecoverage|ad_awsecsservice|ad_awsec2scheduledevents|ad_azureserviceregion|ad_azuresubscription|ad_azurebackupjob|ad_azuresdk|ad_azurewebjob|ad_awsbillingreport|ad_awselasticache|ad_awsredshift|ad_azurebilling|ad_awslbtargetgroups|ad_gcpappengine|ad_gcpbilling|ad_awsvpntunnel|ad_gcpvpntunnel|ad_awsglobalwebacl|ad_gcplbbackendservice|ad_gcppubsubsubscription|ad_gcppubsubsnapshot|ad_azurereplicationjob|ad_azureexpressroutecircuitpeering|ad_awsapigatewaystage|ad_azureautomationaccountcertificate|ad_azurevngconnection|ad_azurewebappinstance|ad_azureappserviceenvironmentmultirolepool|ad_openmetrics|ad_awsmediaconnectoutput|ad_awsmediaconnectsource|ad_awswebaclwafv2|ad_saaso365sharepointsite|ad_awscognitoidentityproviders|ad_azureeabilling|ad_saaszoomplanusage|ad_saasstatus|ad_azuresynapse|ad_saasairbrake|ad_syntheticsselenium|ad_azurevirtualdesktopsessionhosts|ad_saaso365subscribedsku|ad_azuredimension|ad_azurecostmanagementdimensions|ad_saaso365servicehealth|ad_saaso365mailbox|ad_azurenetappvolumes|ad_azureloganalyticsworkspaces|ad_saaszoomstatus|ad_saassalesforcelicense|ad_saaszoomroom|ad_saaswebexlicenseusage|ad_azureloganalyticsreplicationjob|ad_paasjsonpath  # noqa: E501

        :param name: The name of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cluster_dimension(self):
        """Gets the cluster_dimension of this CloudWatchAutoDiscoveryMethod.  # noqa: E501


        :return: The cluster_dimension of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._cluster_dimension

    @cluster_dimension.setter
    def cluster_dimension(self, cluster_dimension):
        """Sets the cluster_dimension of this CloudWatchAutoDiscoveryMethod.


        :param cluster_dimension: The cluster_dimension of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if cluster_dimension is None:
            raise ValueError("Invalid value for `cluster_dimension`, must not be `None`")  # noqa: E501

        self._cluster_dimension = cluster_dimension

    @property
    def period(self):
        """Gets the period of this CloudWatchAutoDiscoveryMethod.  # noqa: E501


        :return: The period of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CloudWatchAutoDiscoveryMethod.


        :param period: The period of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def metric_name(self):
        """Gets the metric_name of this CloudWatchAutoDiscoveryMethod.  # noqa: E501


        :return: The metric_name of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this CloudWatchAutoDiscoveryMethod.


        :param metric_name: The metric_name of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._metric_name = metric_name

    @property
    def node_dimension(self):
        """Gets the node_dimension of this CloudWatchAutoDiscoveryMethod.  # noqa: E501


        :return: The node_dimension of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._node_dimension

    @node_dimension.setter
    def node_dimension(self, node_dimension):
        """Sets the node_dimension of this CloudWatchAutoDiscoveryMethod.


        :param node_dimension: The node_dimension of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if node_dimension is None:
            raise ValueError("Invalid value for `node_dimension`, must not be `None`")  # noqa: E501

        self._node_dimension = node_dimension

    @property
    def namespace(self):
        """Gets the namespace of this CloudWatchAutoDiscoveryMethod.  # noqa: E501


        :return: The namespace of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this CloudWatchAutoDiscoveryMethod.


        :param namespace: The namespace of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")  # noqa: E501

        self._namespace = namespace

    @property
    def cluster_dimension_value(self):
        """Gets the cluster_dimension_value of this CloudWatchAutoDiscoveryMethod.  # noqa: E501


        :return: The cluster_dimension_value of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :rtype: str
        """
        return self._cluster_dimension_value

    @cluster_dimension_value.setter
    def cluster_dimension_value(self, cluster_dimension_value):
        """Sets the cluster_dimension_value of this CloudWatchAutoDiscoveryMethod.


        :param cluster_dimension_value: The cluster_dimension_value of this CloudWatchAutoDiscoveryMethod.  # noqa: E501
        :type: str
        """

        self._cluster_dimension_value = cluster_dimension_value

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
        if issubclass(CloudWatchAutoDiscoveryMethod, dict):
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
        if not isinstance(other, CloudWatchAutoDiscoveryMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
