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


class AccessGroup(object):
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
        'created_by': 'str',
        'name': 'str',
        'tenant_id': 'str',
        'description': 'str',
        'id': 'int',
        'updated_on': 'int',
        'created_on': 'int'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'name': 'name',
        'tenant_id': 'tenantId',
        'description': 'description',
        'id': 'id',
        'updated_on': 'updatedOn',
        'created_on': 'createdOn'
    }

    def __init__(self, created_by=None, name=None, tenant_id=None, description=None, id=None, updated_on=None, created_on=None):  # noqa: E501
        """AccessGroup - a model defined in Swagger"""  # noqa: E501

        self._created_by = None
        self._name = None
        self._tenant_id = None
        self._description = None
        self._id = None
        self._updated_on = None
        self._created_on = None
        self.discriminator = None

        if created_by is not None:
            self.created_by = created_by
        self.name = name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if updated_on is not None:
            self.updated_on = updated_on
        if created_on is not None:
            self.created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this AccessGroup.  # noqa: E501

        User who created access group  # noqa: E501

        :return: The created_by of this AccessGroup.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AccessGroup.

        User who created access group  # noqa: E501

        :param created_by: The created_by of this AccessGroup.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def name(self):
        """Gets the name of this AccessGroup.  # noqa: E501

        The name of the access group  # noqa: E501

        :return: The name of this AccessGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessGroup.

        The name of the access group  # noqa: E501

        :param name: The name of this AccessGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AccessGroup.  # noqa: E501

        Tenancy details  # noqa: E501

        :return: The tenant_id of this AccessGroup.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AccessGroup.

        Tenancy details  # noqa: E501

        :param tenant_id: The tenant_id of this AccessGroup.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def description(self):
        """Gets the description of this AccessGroup.  # noqa: E501

        Description about access group  # noqa: E501

        :return: The description of this AccessGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessGroup.

        Description about access group  # noqa: E501

        :param description: The description of this AccessGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this AccessGroup.  # noqa: E501

        The id of the access group  # noqa: E501

        :return: The id of this AccessGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessGroup.

        The id of the access group  # noqa: E501

        :param id: The id of this AccessGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def updated_on(self):
        """Gets the updated_on of this AccessGroup.  # noqa: E501

        Time when access group updated  # noqa: E501

        :return: The updated_on of this AccessGroup.  # noqa: E501
        :rtype: int
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this AccessGroup.

        Time when access group updated  # noqa: E501

        :param updated_on: The updated_on of this AccessGroup.  # noqa: E501
        :type: int
        """

        self._updated_on = updated_on

    @property
    def created_on(self):
        """Gets the created_on of this AccessGroup.  # noqa: E501

        Time when access group created  # noqa: E501

        :return: The created_on of this AccessGroup.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AccessGroup.

        Time when access group created  # noqa: E501

        :param created_on: The created_on of this AccessGroup.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

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
        if issubclass(AccessGroup, dict):
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
        if not isinstance(other, AccessGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
