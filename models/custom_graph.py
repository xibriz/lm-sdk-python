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

from logicmonitor_sdk.models.custom_flexible_virtual_data_source_ex import CustomFlexibleVirtualDataSourceEx  # noqa: F401,E501
from logicmonitor_sdk.models.custom_virtual_data_point import CustomVirtualDataPoint  # noqa: F401,E501


class CustomGraph(object):
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
        'aggregate': 'object',
        'data_points': 'list[CustomFlexibleVirtualDataSourceEx]',
        'desc': 'object',
        'global_consolidate_function': 'str',
        'id': 'int',
        'max_value': 'object',
        'min_value': 'object',
        'scale_unit': 'int',
        'top_x': 'int',
        'vertical_label': 'str',
        'virtual_data_points': 'list[CustomVirtualDataPoint]'
    }

    attribute_map = {
        'aggregate': 'aggregate',
        'data_points': 'dataPoints',
        'desc': 'desc',
        'global_consolidate_function': 'globalConsolidateFunction',
        'id': 'id',
        'max_value': 'maxValue',
        'min_value': 'minValue',
        'scale_unit': 'scaleUnit',
        'top_x': 'topX',
        'vertical_label': 'verticalLabel',
        'virtual_data_points': 'virtualDataPoints'
    }

    def __init__(self, aggregate=None, data_points=None, desc=None, global_consolidate_function=None, id=None, max_value=None, min_value=None, scale_unit=None, top_x=None, vertical_label=None, virtual_data_points=None):  # noqa: E501
        """CustomGraph - a model defined in Swagger"""  # noqa: E501

        self._aggregate = None
        self._data_points = None
        self._desc = None
        self._global_consolidate_function = None
        self._id = None
        self._max_value = None
        self._min_value = None
        self._scale_unit = None
        self._top_x = None
        self._vertical_label = None
        self._virtual_data_points = None
        self.discriminator = None

        if aggregate is not None:
            self.aggregate = aggregate
        self.data_points = data_points
        if desc is not None:
            self.desc = desc
        if global_consolidate_function is not None:
            self.global_consolidate_function = global_consolidate_function
        if id is not None:
            self.id = id
        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        if scale_unit is not None:
            self.scale_unit = scale_unit
        if top_x is not None:
            self.top_x = top_x
        if vertical_label is not None:
            self.vertical_label = vertical_label
        if virtual_data_points is not None:
            self.virtual_data_points = virtual_data_points

    @property
    def aggregate(self):
        """Gets the aggregate of this CustomGraph.  # noqa: E501

        true: You can set this field to true to aggregate results into one line. false: Results will not be aggregated the default value is true  # noqa: E501

        :return: The aggregate of this CustomGraph.  # noqa: E501
        :rtype: object
        """
        return self._aggregate

    @aggregate.setter
    def aggregate(self, aggregate):
        """Sets the aggregate of this CustomGraph.

        true: You can set this field to true to aggregate results into one line. false: Results will not be aggregated the default value is true  # noqa: E501

        :param aggregate: The aggregate of this CustomGraph.  # noqa: E501
        :type: object
        """

        self._aggregate = aggregate

    @property
    def data_points(self):
        """Gets the data_points of this CustomGraph.  # noqa: E501

        The datapoints added to the widget (note that a datapoint must be referenced in a graph line to be displayed)  # noqa: E501

        :return: The data_points of this CustomGraph.  # noqa: E501
        :rtype: list[CustomFlexibleVirtualDataSourceEx]
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this CustomGraph.

        The datapoints added to the widget (note that a datapoint must be referenced in a graph line to be displayed)  # noqa: E501

        :param data_points: The data_points of this CustomGraph.  # noqa: E501
        :type: list[CustomFlexibleVirtualDataSourceEx]
        """
        if data_points is None:
            raise ValueError("Invalid value for `data_points`, must not be `None`")  # noqa: E501

        self._data_points = data_points

    @property
    def desc(self):
        """Gets the desc of this CustomGraph.  # noqa: E501

        Whether the top X are displayed (false) or the bottom X are displayed (true), the default value is true  # noqa: E501

        :return: The desc of this CustomGraph.  # noqa: E501
        :rtype: object
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this CustomGraph.

        Whether the top X are displayed (false) or the bottom X are displayed (true), the default value is true  # noqa: E501

        :param desc: The desc of this CustomGraph.  # noqa: E501
        :type: object
        """

        self._desc = desc

    @property
    def global_consolidate_function(self):
        """Gets the global_consolidate_function of this CustomGraph.  # noqa: E501

        The function for global consolidate  # noqa: E501

        :return: The global_consolidate_function of this CustomGraph.  # noqa: E501
        :rtype: str
        """
        return self._global_consolidate_function

    @global_consolidate_function.setter
    def global_consolidate_function(self, global_consolidate_function):
        """Sets the global_consolidate_function of this CustomGraph.

        The function for global consolidate  # noqa: E501

        :param global_consolidate_function: The global_consolidate_function of this CustomGraph.  # noqa: E501
        :type: str
        """

        self._global_consolidate_function = global_consolidate_function

    @property
    def id(self):
        """Gets the id of this CustomGraph.  # noqa: E501

        The unique id of the custom graph displayed by this widget (not to be confused with the widget id)  # noqa: E501

        :return: The id of this CustomGraph.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomGraph.

        The unique id of the custom graph displayed by this widget (not to be confused with the widget id)  # noqa: E501

        :param id: The id of this CustomGraph.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def max_value(self):
        """Gets the max_value of this CustomGraph.  # noqa: E501

        The maximum value that should be displayed on the y-axis  # noqa: E501

        :return: The max_value of this CustomGraph.  # noqa: E501
        :rtype: object
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this CustomGraph.

        The maximum value that should be displayed on the y-axis  # noqa: E501

        :param max_value: The max_value of this CustomGraph.  # noqa: E501
        :type: object
        """

        self._max_value = max_value

    @property
    def min_value(self):
        """Gets the min_value of this CustomGraph.  # noqa: E501

        The minimum value that should be displayed on the y-axis  # noqa: E501

        :return: The min_value of this CustomGraph.  # noqa: E501
        :rtype: object
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this CustomGraph.

        The minimum value that should be displayed on the y-axis  # noqa: E501

        :param min_value: The min_value of this CustomGraph.  # noqa: E501
        :type: object
        """

        self._min_value = min_value

    @property
    def scale_unit(self):
        """Gets the scale_unit of this CustomGraph.  # noqa: E501

        The base scale unit (1000 or 1024)  # noqa: E501

        :return: The scale_unit of this CustomGraph.  # noqa: E501
        :rtype: int
        """
        return self._scale_unit

    @scale_unit.setter
    def scale_unit(self, scale_unit):
        """Sets the scale_unit of this CustomGraph.

        The base scale unit (1000 or 1024)  # noqa: E501

        :param scale_unit: The scale_unit of this CustomGraph.  # noqa: E501
        :type: int
        """

        self._scale_unit = scale_unit

    @property
    def top_x(self):
        """Gets the top_x of this CustomGraph.  # noqa: E501

        The number of lines to display for each configured datapoint  # noqa: E501

        :return: The top_x of this CustomGraph.  # noqa: E501
        :rtype: int
        """
        return self._top_x

    @top_x.setter
    def top_x(self, top_x):
        """Sets the top_x of this CustomGraph.

        The number of lines to display for each configured datapoint  # noqa: E501

        :param top_x: The top_x of this CustomGraph.  # noqa: E501
        :type: int
        """

        self._top_x = top_x

    @property
    def vertical_label(self):
        """Gets the vertical_label of this CustomGraph.  # noqa: E501

        The label that will be display along the y axis  # noqa: E501

        :return: The vertical_label of this CustomGraph.  # noqa: E501
        :rtype: str
        """
        return self._vertical_label

    @vertical_label.setter
    def vertical_label(self, vertical_label):
        """Sets the vertical_label of this CustomGraph.

        The label that will be display along the y axis  # noqa: E501

        :param vertical_label: The vertical_label of this CustomGraph.  # noqa: E501
        :type: str
        """

        self._vertical_label = vertical_label

    @property
    def virtual_data_points(self):
        """Gets the virtual_data_points of this CustomGraph.  # noqa: E501

        The virtual datapoints added to the widget (note that a virtual datapoint must be referenced in a graph line to be displayed)  # noqa: E501

        :return: The virtual_data_points of this CustomGraph.  # noqa: E501
        :rtype: list[CustomVirtualDataPoint]
        """
        return self._virtual_data_points

    @virtual_data_points.setter
    def virtual_data_points(self, virtual_data_points):
        """Sets the virtual_data_points of this CustomGraph.

        The virtual datapoints added to the widget (note that a virtual datapoint must be referenced in a graph line to be displayed)  # noqa: E501

        :param virtual_data_points: The virtual_data_points of this CustomGraph.  # noqa: E501
        :type: list[CustomVirtualDataPoint]
        """

        self._virtual_data_points = virtual_data_points

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
        if issubclass(CustomGraph, dict):
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
        if not isinstance(other, CustomGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
