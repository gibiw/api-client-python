"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import testit_api_client
from testit_api_client.model.auto_test_model import AutoTestModel
from testit_api_client.model.test_plan_model import TestPlanModel
from testit_api_client.model.test_result_model import TestResultModel
from testit_api_client.model.test_run_analytic_result_model import TestRunAnalyticResultModel
from testit_api_client.model.test_run_state_type_model import TestRunStateTypeModel
globals()['AutoTestModel'] = AutoTestModel
globals()['TestPlanModel'] = TestPlanModel
globals()['TestResultModel'] = TestResultModel
globals()['TestRunAnalyticResultModel'] = TestRunAnalyticResultModel
globals()['TestRunStateTypeModel'] = TestRunStateTypeModel
from testit_api_client.model.test_run_model import TestRunModel


class TestTestRunModel(unittest.TestCase):
    """TestRunModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTestRunModel(self):
        """Test TestRunModel"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TestRunModel()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
