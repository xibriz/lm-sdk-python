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


class GenerateReportResult(object):
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
        'report_id': 'int',
        'task_id': 'int',
        'resulturl': 'str'
    }

    attribute_map = {
        'report_id': 'reportId',
        'task_id': 'taskId',
        'resulturl': 'resulturl'
    }

    def __init__(self, report_id=None, task_id=None, resulturl=None):  # noqa: E501
        """GenerateReportResult - a model defined in Swagger"""  # noqa: E501

        self._report_id = None
        self._task_id = None
        self._resulturl = None
        self.discriminator = None

        self.report_id = report_id
        self.task_id = task_id
        if resulturl is not None:
            self.resulturl = resulturl

    @property
    def report_id(self):
        """Gets the report_id of this GenerateReportResult.  # noqa: E501

        The id of the report  # noqa: E501

        :return: The report_id of this GenerateReportResult.  # noqa: E501
        :rtype: int
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this GenerateReportResult.

        The id of the report  # noqa: E501

        :param report_id: The report_id of this GenerateReportResult.  # noqa: E501
        :type: int
        """
        if report_id is None:
            raise ValueError("Invalid value for `report_id`, must not be `None`")  # noqa: E501

        self._report_id = report_id

    @property
    def task_id(self):
        """Gets the task_id of this GenerateReportResult.  # noqa: E501

        The task id of the generating process  # noqa: E501

        :return: The task_id of this GenerateReportResult.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this GenerateReportResult.

        The task id of the generating process  # noqa: E501

        :param task_id: The task_id of this GenerateReportResult.  # noqa: E501
        :type: int
        """
        if task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501

        self._task_id = task_id

    @property
    def resulturl(self):
        """Gets the resulturl of this GenerateReportResult.  # noqa: E501

        The url of the generated report  # noqa: E501

        :return: The resulturl of this GenerateReportResult.  # noqa: E501
        :rtype: str
        """
        return self._resulturl

    @resulturl.setter
    def resulturl(self, resulturl):
        """Sets the resulturl of this GenerateReportResult.

        The url of the generated report  # noqa: E501

        :param resulturl: The resulturl of this GenerateReportResult.  # noqa: E501
        :type: str
        """

        self._resulturl = resulturl

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
        if issubclass(GenerateReportResult, dict):
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
        if not isinstance(other, GenerateReportResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
