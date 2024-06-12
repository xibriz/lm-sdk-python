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


class RestAzureStorageAccountVerify(object):
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
        'client_id': 'str',
        'secret_key': 'str',
        'china_account': 'bool',
        'tenant_id': 'str',
        'storage_account_name': 'str',
        'storage_account_container_name': 'str',
        'is_china_account': 'bool'
    }

    attribute_map = {
        'client_id': 'clientId',
        'secret_key': 'secretKey',
        'china_account': 'chinaAccount',
        'tenant_id': 'tenantId',
        'storage_account_name': 'storageAccountName',
        'storage_account_container_name': 'storageAccountContainerName',
        'is_china_account': 'isChinaAccount'
    }

    def __init__(self, client_id=None, secret_key=None, china_account=None, tenant_id=None, storage_account_name=None, storage_account_container_name=None, is_china_account=None):  # noqa: E501
        """RestAzureStorageAccountVerify - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._secret_key = None
        self._china_account = None
        self._tenant_id = None
        self._storage_account_name = None
        self._storage_account_container_name = None
        self._is_china_account = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if secret_key is not None:
            self.secret_key = secret_key
        if china_account is not None:
            self.china_account = china_account
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if storage_account_name is not None:
            self.storage_account_name = storage_account_name
        if storage_account_container_name is not None:
            self.storage_account_container_name = storage_account_container_name
        if is_china_account is not None:
            self.is_china_account = is_china_account

    @property
    def client_id(self):
        """Gets the client_id of this RestAzureStorageAccountVerify.  # noqa: E501


        :return: The client_id of this RestAzureStorageAccountVerify.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this RestAzureStorageAccountVerify.


        :param client_id: The client_id of this RestAzureStorageAccountVerify.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def secret_key(self):
        """Gets the secret_key of this RestAzureStorageAccountVerify.  # noqa: E501


        :return: The secret_key of this RestAzureStorageAccountVerify.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this RestAzureStorageAccountVerify.


        :param secret_key: The secret_key of this RestAzureStorageAccountVerify.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def china_account(self):
        """Gets the china_account of this RestAzureStorageAccountVerify.  # noqa: E501


        :return: The china_account of this RestAzureStorageAccountVerify.  # noqa: E501
        :rtype: bool
        """
        return self._china_account

    @china_account.setter
    def china_account(self, china_account):
        """Sets the china_account of this RestAzureStorageAccountVerify.


        :param china_account: The china_account of this RestAzureStorageAccountVerify.  # noqa: E501
        :type: bool
        """

        self._china_account = china_account

    @property
    def tenant_id(self):
        """Gets the tenant_id of this RestAzureStorageAccountVerify.  # noqa: E501


        :return: The tenant_id of this RestAzureStorageAccountVerify.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this RestAzureStorageAccountVerify.


        :param tenant_id: The tenant_id of this RestAzureStorageAccountVerify.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def storage_account_name(self):
        """Gets the storage_account_name of this RestAzureStorageAccountVerify.  # noqa: E501


        :return: The storage_account_name of this RestAzureStorageAccountVerify.  # noqa: E501
        :rtype: str
        """
        return self._storage_account_name

    @storage_account_name.setter
    def storage_account_name(self, storage_account_name):
        """Sets the storage_account_name of this RestAzureStorageAccountVerify.


        :param storage_account_name: The storage_account_name of this RestAzureStorageAccountVerify.  # noqa: E501
        :type: str
        """

        self._storage_account_name = storage_account_name

    @property
    def storage_account_container_name(self):
        """Gets the storage_account_container_name of this RestAzureStorageAccountVerify.  # noqa: E501


        :return: The storage_account_container_name of this RestAzureStorageAccountVerify.  # noqa: E501
        :rtype: str
        """
        return self._storage_account_container_name

    @storage_account_container_name.setter
    def storage_account_container_name(self, storage_account_container_name):
        """Sets the storage_account_container_name of this RestAzureStorageAccountVerify.


        :param storage_account_container_name: The storage_account_container_name of this RestAzureStorageAccountVerify.  # noqa: E501
        :type: str
        """

        self._storage_account_container_name = storage_account_container_name

    @property
    def is_china_account(self):
        """Gets the is_china_account of this RestAzureStorageAccountVerify.  # noqa: E501


        :return: The is_china_account of this RestAzureStorageAccountVerify.  # noqa: E501
        :rtype: bool
        """
        return self._is_china_account

    @is_china_account.setter
    def is_china_account(self, is_china_account):
        """Sets the is_china_account of this RestAzureStorageAccountVerify.


        :param is_china_account: The is_china_account of this RestAzureStorageAccountVerify.  # noqa: E501
        :type: bool
        """

        self._is_china_account = is_china_account

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
        if issubclass(RestAzureStorageAccountVerify, dict):
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
        if not isinstance(other, RestAzureStorageAccountVerify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
