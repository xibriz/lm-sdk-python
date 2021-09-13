# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically. Note: For Python SDKs, the REQUEST parameters can contain camelCase or an underscore. However, the RESPONSE parameters will always contain an underscore. For example, the REQUEST parameter can be testLocation or test_location. The RESPONSE parameter will be test_location.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import logicmonitor_sdk
from logicmonitor_sdk.models.ntlm_authentication import NTLMAuthentication  # noqa: E501
from logicmonitor_sdk.rest import ApiException


class TestNTLMAuthentication(unittest.TestCase):
    """NTLMAuthentication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNTLMAuthentication(self):
        """Test NTLMAuthentication"""
        # FIXME: construct object with mandatory attributes with example values
        # model = logicmonitor_sdk.models.ntlm_authentication.NTLMAuthentication()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
