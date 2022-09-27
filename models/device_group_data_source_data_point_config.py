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


class DeviceGroupDataSourceDataPointConfig(object):
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
        'global_alert_expr': 'str',
        'enable_anomaly_alert_suppression': 'str',
        'critical_ad_adv_setting': 'str',
        'disable_alerting': 'bool',
        'alert_expr_note': 'str',
        'ad_adv_setting_enabled': 'bool',
        'error_ad_adv_setting': 'str',
        'data_point_description': 'str',
        'global_enable_anomaly_alert_generation': 'str',
        'enable_anomaly_alert_generation': 'str',
        'warn_ad_adv_setting': 'str',
        'data_point_name': 'str',
        'data_point_id': 'int',
        'global_enable_anomaly_alert_suppression': 'str',
        'collection_interval': 'int',
        'alert_expr': 'str'
    }

    attribute_map = {
        'global_alert_expr': 'globalAlertExpr',
        'enable_anomaly_alert_suppression': 'enableAnomalyAlertSuppression',
        'critical_ad_adv_setting': 'criticalAdAdvSetting',
        'disable_alerting': 'disableAlerting',
        'alert_expr_note': 'alertExprNote',
        'ad_adv_setting_enabled': 'adAdvSettingEnabled',
        'error_ad_adv_setting': 'errorAdAdvSetting',
        'data_point_description': 'dataPointDescription',
        'global_enable_anomaly_alert_generation': 'globalEnableAnomalyAlertGeneration',
        'enable_anomaly_alert_generation': 'enableAnomalyAlertGeneration',
        'warn_ad_adv_setting': 'warnAdAdvSetting',
        'data_point_name': 'dataPointName',
        'data_point_id': 'dataPointId',
        'global_enable_anomaly_alert_suppression': 'globalEnableAnomalyAlertSuppression',
        'collection_interval': 'collectionInterval',
        'alert_expr': 'alertExpr'
    }

    def __init__(self, global_alert_expr=None, enable_anomaly_alert_suppression=None, critical_ad_adv_setting=None, disable_alerting=None, alert_expr_note=None, ad_adv_setting_enabled=None, error_ad_adv_setting=None, data_point_description=None, global_enable_anomaly_alert_generation=None, enable_anomaly_alert_generation=None, warn_ad_adv_setting=None, data_point_name=None, data_point_id=None, global_enable_anomaly_alert_suppression=None, collection_interval=None, alert_expr=None):  # noqa: E501
        """DeviceGroupDataSourceDataPointConfig - a model defined in Swagger"""  # noqa: E501

        self._global_alert_expr = None
        self._enable_anomaly_alert_suppression = None
        self._critical_ad_adv_setting = None
        self._disable_alerting = None
        self._alert_expr_note = None
        self._ad_adv_setting_enabled = None
        self._error_ad_adv_setting = None
        self._data_point_description = None
        self._global_enable_anomaly_alert_generation = None
        self._enable_anomaly_alert_generation = None
        self._warn_ad_adv_setting = None
        self._data_point_name = None
        self._data_point_id = None
        self._global_enable_anomaly_alert_suppression = None
        self._collection_interval = None
        self._alert_expr = None
        self.discriminator = None

        if global_alert_expr is not None:
            self.global_alert_expr = global_alert_expr
        if enable_anomaly_alert_suppression is not None:
            self.enable_anomaly_alert_suppression = enable_anomaly_alert_suppression
        if critical_ad_adv_setting is not None:
            self.critical_ad_adv_setting = critical_ad_adv_setting
        if disable_alerting is not None:
            self.disable_alerting = disable_alerting
        if alert_expr_note is not None:
            self.alert_expr_note = alert_expr_note
        if ad_adv_setting_enabled is not None:
            self.ad_adv_setting_enabled = ad_adv_setting_enabled
        if error_ad_adv_setting is not None:
            self.error_ad_adv_setting = error_ad_adv_setting
        if data_point_description is not None:
            self.data_point_description = data_point_description
        if global_enable_anomaly_alert_generation is not None:
            self.global_enable_anomaly_alert_generation = global_enable_anomaly_alert_generation
        if enable_anomaly_alert_generation is not None:
            self.enable_anomaly_alert_generation = enable_anomaly_alert_generation
        if warn_ad_adv_setting is not None:
            self.warn_ad_adv_setting = warn_ad_adv_setting
        self.data_point_name = data_point_name
        self.data_point_id = data_point_id
        if global_enable_anomaly_alert_suppression is not None:
            self.global_enable_anomaly_alert_suppression = global_enable_anomaly_alert_suppression
        if collection_interval is not None:
            self.collection_interval = collection_interval
        self.alert_expr = alert_expr

    @property
    def global_alert_expr(self):
        """Gets the global_alert_expr of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The global_alert_expr of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._global_alert_expr

    @global_alert_expr.setter
    def global_alert_expr(self, global_alert_expr):
        """Sets the global_alert_expr of this DeviceGroupDataSourceDataPointConfig.


        :param global_alert_expr: The global_alert_expr of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._global_alert_expr = global_alert_expr

    @property
    def enable_anomaly_alert_suppression(self):
        """Gets the enable_anomaly_alert_suppression of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The enable_anomaly_alert_suppression of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._enable_anomaly_alert_suppression

    @enable_anomaly_alert_suppression.setter
    def enable_anomaly_alert_suppression(self, enable_anomaly_alert_suppression):
        """Sets the enable_anomaly_alert_suppression of this DeviceGroupDataSourceDataPointConfig.


        :param enable_anomaly_alert_suppression: The enable_anomaly_alert_suppression of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._enable_anomaly_alert_suppression = enable_anomaly_alert_suppression

    @property
    def critical_ad_adv_setting(self):
        """Gets the critical_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The critical_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._critical_ad_adv_setting

    @critical_ad_adv_setting.setter
    def critical_ad_adv_setting(self, critical_ad_adv_setting):
        """Sets the critical_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.


        :param critical_ad_adv_setting: The critical_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._critical_ad_adv_setting = critical_ad_adv_setting

    @property
    def disable_alerting(self):
        """Gets the disable_alerting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The disable_alerting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: bool
        """
        return self._disable_alerting

    @disable_alerting.setter
    def disable_alerting(self, disable_alerting):
        """Sets the disable_alerting of this DeviceGroupDataSourceDataPointConfig.


        :param disable_alerting: The disable_alerting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: bool
        """

        self._disable_alerting = disable_alerting

    @property
    def alert_expr_note(self):
        """Gets the alert_expr_note of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The alert_expr_note of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._alert_expr_note

    @alert_expr_note.setter
    def alert_expr_note(self, alert_expr_note):
        """Sets the alert_expr_note of this DeviceGroupDataSourceDataPointConfig.


        :param alert_expr_note: The alert_expr_note of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._alert_expr_note = alert_expr_note

    @property
    def ad_adv_setting_enabled(self):
        """Gets the ad_adv_setting_enabled of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The ad_adv_setting_enabled of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: bool
        """
        return self._ad_adv_setting_enabled

    @ad_adv_setting_enabled.setter
    def ad_adv_setting_enabled(self, ad_adv_setting_enabled):
        """Sets the ad_adv_setting_enabled of this DeviceGroupDataSourceDataPointConfig.


        :param ad_adv_setting_enabled: The ad_adv_setting_enabled of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: bool
        """

        self._ad_adv_setting_enabled = ad_adv_setting_enabled

    @property
    def error_ad_adv_setting(self):
        """Gets the error_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The error_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._error_ad_adv_setting

    @error_ad_adv_setting.setter
    def error_ad_adv_setting(self, error_ad_adv_setting):
        """Sets the error_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.


        :param error_ad_adv_setting: The error_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._error_ad_adv_setting = error_ad_adv_setting

    @property
    def data_point_description(self):
        """Gets the data_point_description of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The data_point_description of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._data_point_description

    @data_point_description.setter
    def data_point_description(self, data_point_description):
        """Sets the data_point_description of this DeviceGroupDataSourceDataPointConfig.


        :param data_point_description: The data_point_description of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._data_point_description = data_point_description

    @property
    def global_enable_anomaly_alert_generation(self):
        """Gets the global_enable_anomaly_alert_generation of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The global_enable_anomaly_alert_generation of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._global_enable_anomaly_alert_generation

    @global_enable_anomaly_alert_generation.setter
    def global_enable_anomaly_alert_generation(self, global_enable_anomaly_alert_generation):
        """Sets the global_enable_anomaly_alert_generation of this DeviceGroupDataSourceDataPointConfig.


        :param global_enable_anomaly_alert_generation: The global_enable_anomaly_alert_generation of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._global_enable_anomaly_alert_generation = global_enable_anomaly_alert_generation

    @property
    def enable_anomaly_alert_generation(self):
        """Gets the enable_anomaly_alert_generation of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The enable_anomaly_alert_generation of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._enable_anomaly_alert_generation

    @enable_anomaly_alert_generation.setter
    def enable_anomaly_alert_generation(self, enable_anomaly_alert_generation):
        """Sets the enable_anomaly_alert_generation of this DeviceGroupDataSourceDataPointConfig.


        :param enable_anomaly_alert_generation: The enable_anomaly_alert_generation of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._enable_anomaly_alert_generation = enable_anomaly_alert_generation

    @property
    def warn_ad_adv_setting(self):
        """Gets the warn_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The warn_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._warn_ad_adv_setting

    @warn_ad_adv_setting.setter
    def warn_ad_adv_setting(self, warn_ad_adv_setting):
        """Sets the warn_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.


        :param warn_ad_adv_setting: The warn_ad_adv_setting of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._warn_ad_adv_setting = warn_ad_adv_setting

    @property
    def data_point_name(self):
        """Gets the data_point_name of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The data_point_name of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._data_point_name

    @data_point_name.setter
    def data_point_name(self, data_point_name):
        """Sets the data_point_name of this DeviceGroupDataSourceDataPointConfig.


        :param data_point_name: The data_point_name of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """
        if data_point_name is None:
            raise ValueError("Invalid value for `data_point_name`, must not be `None`")  # noqa: E501

        self._data_point_name = data_point_name

    @property
    def data_point_id(self):
        """Gets the data_point_id of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The data_point_id of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: int
        """
        return self._data_point_id

    @data_point_id.setter
    def data_point_id(self, data_point_id):
        """Sets the data_point_id of this DeviceGroupDataSourceDataPointConfig.


        :param data_point_id: The data_point_id of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: int
        """
        if data_point_id is None:
            raise ValueError("Invalid value for `data_point_id`, must not be `None`")  # noqa: E501

        self._data_point_id = data_point_id

    @property
    def global_enable_anomaly_alert_suppression(self):
        """Gets the global_enable_anomaly_alert_suppression of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The global_enable_anomaly_alert_suppression of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._global_enable_anomaly_alert_suppression

    @global_enable_anomaly_alert_suppression.setter
    def global_enable_anomaly_alert_suppression(self, global_enable_anomaly_alert_suppression):
        """Sets the global_enable_anomaly_alert_suppression of this DeviceGroupDataSourceDataPointConfig.


        :param global_enable_anomaly_alert_suppression: The global_enable_anomaly_alert_suppression of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """

        self._global_enable_anomaly_alert_suppression = global_enable_anomaly_alert_suppression

    @property
    def collection_interval(self):
        """Gets the collection_interval of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501

        Collection Interval  # noqa: E501

        :return: The collection_interval of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: int
        """
        return self._collection_interval

    @collection_interval.setter
    def collection_interval(self, collection_interval):
        """Sets the collection_interval of this DeviceGroupDataSourceDataPointConfig.

        Collection Interval  # noqa: E501

        :param collection_interval: The collection_interval of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: int
        """

        self._collection_interval = collection_interval

    @property
    def alert_expr(self):
        """Gets the alert_expr of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501


        :return: The alert_expr of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :rtype: str
        """
        return self._alert_expr

    @alert_expr.setter
    def alert_expr(self, alert_expr):
        """Sets the alert_expr of this DeviceGroupDataSourceDataPointConfig.


        :param alert_expr: The alert_expr of this DeviceGroupDataSourceDataPointConfig.  # noqa: E501
        :type: str
        """
        if alert_expr is None:
            raise ValueError("Invalid value for `alert_expr`, must not be `None`")  # noqa: E501

        self._alert_expr = alert_expr

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
        if issubclass(DeviceGroupDataSourceDataPointConfig, dict):
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
        if not isinstance(other, DeviceGroupDataSourceDataPointConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
