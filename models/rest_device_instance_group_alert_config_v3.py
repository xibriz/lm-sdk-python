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


class RestDeviceInstanceGroupAlertConfigV3(object):
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
        'alert_for_no_data': 'int',
        'enable_anomaly_alert_suppression': 'str',
        'global_alert_for_no_data': 'int',
        'alert_enable': 'bool',
        'critical_ad_adv_setting': 'str',
        'alert_clear_transition_interval': 'int',
        'global_alert_transition_interval': 'int',
        'alert_expr_note': 'str',
        'ad_adv_setting_enabled': 'bool',
        'error_ad_adv_setting': 'str',
        'warn_ad_adv_setting': 'str',
        'global_alert_clear_transition_interval': 'int',
        'alert_expr': 'str',
        'alert_transition_interval': 'int'
    }

    attribute_map = {
        'alert_for_no_data': 'alertForNoData',
        'enable_anomaly_alert_suppression': 'enableAnomalyAlertSuppression',
        'global_alert_for_no_data': 'globalAlertForNoData',
        'alert_enable': 'alertEnable',
        'critical_ad_adv_setting': 'criticalAdAdvSetting',
        'alert_clear_transition_interval': 'alertClearTransitionInterval',
        'global_alert_transition_interval': 'globalAlertTransitionInterval',
        'alert_expr_note': 'alertExprNote',
        'ad_adv_setting_enabled': 'adAdvSettingEnabled',
        'error_ad_adv_setting': 'errorAdAdvSetting',
        'warn_ad_adv_setting': 'warnAdAdvSetting',
        'global_alert_clear_transition_interval': 'globalAlertClearTransitionInterval',
        'alert_expr': 'alertExpr',
        'alert_transition_interval': 'alertTransitionInterval'
    }

    def __init__(self, alert_for_no_data=None, enable_anomaly_alert_suppression=None, global_alert_for_no_data=None, alert_enable=None, critical_ad_adv_setting=None, alert_clear_transition_interval=None, global_alert_transition_interval=None, alert_expr_note=None, ad_adv_setting_enabled=None, error_ad_adv_setting=None, warn_ad_adv_setting=None, global_alert_clear_transition_interval=None, alert_expr=None, alert_transition_interval=None):  # noqa: E501
        """RestDeviceInstanceGroupAlertConfigV3 - a model defined in Swagger"""  # noqa: E501

        self._alert_for_no_data = None
        self._enable_anomaly_alert_suppression = None
        self._global_alert_for_no_data = None
        self._alert_enable = None
        self._critical_ad_adv_setting = None
        self._alert_clear_transition_interval = None
        self._global_alert_transition_interval = None
        self._alert_expr_note = None
        self._ad_adv_setting_enabled = None
        self._error_ad_adv_setting = None
        self._warn_ad_adv_setting = None
        self._global_alert_clear_transition_interval = None
        self._alert_expr = None
        self._alert_transition_interval = None
        self.discriminator = None

        if alert_for_no_data is not None:
            self.alert_for_no_data = alert_for_no_data
        if enable_anomaly_alert_suppression is not None:
            self.enable_anomaly_alert_suppression = enable_anomaly_alert_suppression
        if global_alert_for_no_data is not None:
            self.global_alert_for_no_data = global_alert_for_no_data
        if alert_enable is not None:
            self.alert_enable = alert_enable
        if critical_ad_adv_setting is not None:
            self.critical_ad_adv_setting = critical_ad_adv_setting
        if alert_clear_transition_interval is not None:
            self.alert_clear_transition_interval = alert_clear_transition_interval
        if global_alert_transition_interval is not None:
            self.global_alert_transition_interval = global_alert_transition_interval
        if alert_expr_note is not None:
            self.alert_expr_note = alert_expr_note
        if ad_adv_setting_enabled is not None:
            self.ad_adv_setting_enabled = ad_adv_setting_enabled
        if error_ad_adv_setting is not None:
            self.error_ad_adv_setting = error_ad_adv_setting
        if warn_ad_adv_setting is not None:
            self.warn_ad_adv_setting = warn_ad_adv_setting
        if global_alert_clear_transition_interval is not None:
            self.global_alert_clear_transition_interval = global_alert_clear_transition_interval
        if alert_expr is not None:
            self.alert_expr = alert_expr
        if alert_transition_interval is not None:
            self.alert_transition_interval = alert_transition_interval

    @property
    def alert_for_no_data(self):
        """Gets the alert_for_no_data of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501

        The triggered alert level if we cannot collect data for this datapoint. The values can be 1-4 (1:no alert, 2:warn alert, 3:error alert, 4:critical alert)  # noqa: E501

        :return: The alert_for_no_data of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: int
        """
        return self._alert_for_no_data

    @alert_for_no_data.setter
    def alert_for_no_data(self, alert_for_no_data):
        """Sets the alert_for_no_data of this RestDeviceInstanceGroupAlertConfigV3.

        The triggered alert level if we cannot collect data for this datapoint. The values can be 1-4 (1:no alert, 2:warn alert, 3:error alert, 4:critical alert)  # noqa: E501

        :param alert_for_no_data: The alert_for_no_data of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: int
        """

        self._alert_for_no_data = alert_for_no_data

    @property
    def enable_anomaly_alert_suppression(self):
        """Gets the enable_anomaly_alert_suppression of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501


        :return: The enable_anomaly_alert_suppression of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: str
        """
        return self._enable_anomaly_alert_suppression

    @enable_anomaly_alert_suppression.setter
    def enable_anomaly_alert_suppression(self, enable_anomaly_alert_suppression):
        """Sets the enable_anomaly_alert_suppression of this RestDeviceInstanceGroupAlertConfigV3.


        :param enable_anomaly_alert_suppression: The enable_anomaly_alert_suppression of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: str
        """

        self._enable_anomaly_alert_suppression = enable_anomaly_alert_suppression

    @property
    def global_alert_for_no_data(self):
        """Gets the global_alert_for_no_data of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501

        The triggered alert level if we cannot collect data for this datapoint. The values can be 1-4 (1:no alert, 2:warn alert, 3:error alert, 4:critical alert)  # noqa: E501

        :return: The global_alert_for_no_data of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: int
        """
        return self._global_alert_for_no_data

    @global_alert_for_no_data.setter
    def global_alert_for_no_data(self, global_alert_for_no_data):
        """Sets the global_alert_for_no_data of this RestDeviceInstanceGroupAlertConfigV3.

        The triggered alert level if we cannot collect data for this datapoint. The values can be 1-4 (1:no alert, 2:warn alert, 3:error alert, 4:critical alert)  # noqa: E501

        :param global_alert_for_no_data: The global_alert_for_no_data of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: int
        """

        self._global_alert_for_no_data = global_alert_for_no_data

    @property
    def alert_enable(self):
        """Gets the alert_enable of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501


        :return: The alert_enable of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: bool
        """
        return self._alert_enable

    @alert_enable.setter
    def alert_enable(self, alert_enable):
        """Sets the alert_enable of this RestDeviceInstanceGroupAlertConfigV3.


        :param alert_enable: The alert_enable of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: bool
        """

        self._alert_enable = alert_enable

    @property
    def critical_ad_adv_setting(self):
        """Gets the critical_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501


        :return: The critical_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: str
        """
        return self._critical_ad_adv_setting

    @critical_ad_adv_setting.setter
    def critical_ad_adv_setting(self, critical_ad_adv_setting):
        """Sets the critical_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.


        :param critical_ad_adv_setting: The critical_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: str
        """

        self._critical_ad_adv_setting = critical_ad_adv_setting

    @property
    def alert_clear_transition_interval(self):
        """Gets the alert_clear_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501

        The count that the alert must exist for this many poll cycles before the alert will be cleared (0-60)  # noqa: E501

        :return: The alert_clear_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: int
        """
        return self._alert_clear_transition_interval

    @alert_clear_transition_interval.setter
    def alert_clear_transition_interval(self, alert_clear_transition_interval):
        """Sets the alert_clear_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.

        The count that the alert must exist for this many poll cycles before the alert will be cleared (0-60)  # noqa: E501

        :param alert_clear_transition_interval: The alert_clear_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: int
        """

        self._alert_clear_transition_interval = alert_clear_transition_interval

    @property
    def global_alert_transition_interval(self):
        """Gets the global_alert_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501

        The count that the alert must exist for this many poll cycles before it will be triggered  # noqa: E501

        :return: The global_alert_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: int
        """
        return self._global_alert_transition_interval

    @global_alert_transition_interval.setter
    def global_alert_transition_interval(self, global_alert_transition_interval):
        """Sets the global_alert_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.

        The count that the alert must exist for this many poll cycles before it will be triggered  # noqa: E501

        :param global_alert_transition_interval: The global_alert_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: int
        """

        self._global_alert_transition_interval = global_alert_transition_interval

    @property
    def alert_expr_note(self):
        """Gets the alert_expr_note of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501


        :return: The alert_expr_note of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: str
        """
        return self._alert_expr_note

    @alert_expr_note.setter
    def alert_expr_note(self, alert_expr_note):
        """Sets the alert_expr_note of this RestDeviceInstanceGroupAlertConfigV3.


        :param alert_expr_note: The alert_expr_note of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: str
        """

        self._alert_expr_note = alert_expr_note

    @property
    def ad_adv_setting_enabled(self):
        """Gets the ad_adv_setting_enabled of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501


        :return: The ad_adv_setting_enabled of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: bool
        """
        return self._ad_adv_setting_enabled

    @ad_adv_setting_enabled.setter
    def ad_adv_setting_enabled(self, ad_adv_setting_enabled):
        """Sets the ad_adv_setting_enabled of this RestDeviceInstanceGroupAlertConfigV3.


        :param ad_adv_setting_enabled: The ad_adv_setting_enabled of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: bool
        """

        self._ad_adv_setting_enabled = ad_adv_setting_enabled

    @property
    def error_ad_adv_setting(self):
        """Gets the error_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501


        :return: The error_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: str
        """
        return self._error_ad_adv_setting

    @error_ad_adv_setting.setter
    def error_ad_adv_setting(self, error_ad_adv_setting):
        """Sets the error_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.


        :param error_ad_adv_setting: The error_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: str
        """

        self._error_ad_adv_setting = error_ad_adv_setting

    @property
    def warn_ad_adv_setting(self):
        """Gets the warn_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501


        :return: The warn_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: str
        """
        return self._warn_ad_adv_setting

    @warn_ad_adv_setting.setter
    def warn_ad_adv_setting(self, warn_ad_adv_setting):
        """Sets the warn_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.


        :param warn_ad_adv_setting: The warn_ad_adv_setting of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: str
        """

        self._warn_ad_adv_setting = warn_ad_adv_setting

    @property
    def global_alert_clear_transition_interval(self):
        """Gets the global_alert_clear_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501

        The count that the alert must exist for this many poll cycles before the alert will be cleared  # noqa: E501

        :return: The global_alert_clear_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: int
        """
        return self._global_alert_clear_transition_interval

    @global_alert_clear_transition_interval.setter
    def global_alert_clear_transition_interval(self, global_alert_clear_transition_interval):
        """Sets the global_alert_clear_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.

        The count that the alert must exist for this many poll cycles before the alert will be cleared  # noqa: E501

        :param global_alert_clear_transition_interval: The global_alert_clear_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: int
        """

        self._global_alert_clear_transition_interval = global_alert_clear_transition_interval

    @property
    def alert_expr(self):
        """Gets the alert_expr of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501


        :return: The alert_expr of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: str
        """
        return self._alert_expr

    @alert_expr.setter
    def alert_expr(self, alert_expr):
        """Sets the alert_expr of this RestDeviceInstanceGroupAlertConfigV3.


        :param alert_expr: The alert_expr of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: str
        """

        self._alert_expr = alert_expr

    @property
    def alert_transition_interval(self):
        """Gets the alert_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501

        The count that the alert must exist for this many poll cycles before it will be triggered (0-60)  # noqa: E501

        :return: The alert_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :rtype: int
        """
        return self._alert_transition_interval

    @alert_transition_interval.setter
    def alert_transition_interval(self, alert_transition_interval):
        """Sets the alert_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.

        The count that the alert must exist for this many poll cycles before it will be triggered (0-60)  # noqa: E501

        :param alert_transition_interval: The alert_transition_interval of this RestDeviceInstanceGroupAlertConfigV3.  # noqa: E501
        :type: int
        """

        self._alert_transition_interval = alert_transition_interval

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
        if issubclass(RestDeviceInstanceGroupAlertConfigV3, dict):
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
        if not isinstance(other, RestDeviceInstanceGroupAlertConfigV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
