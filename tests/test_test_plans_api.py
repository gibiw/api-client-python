"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import testit_api_client
from testit_api_client.api.test_plans_api import TestPlansApi  # noqa: E501


class TestTestPlansApi(unittest.TestCase):
    """TestPlansApi unit test stubs"""

    def setUp(self):
        self.api = TestPlansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_test_points_with_sections(self):
        """Test case for add_test_points_with_sections

        Add test-points to test suite with sections  # noqa: E501
        """
        pass

    def test_add_work_items_with_sections(self):
        """Test case for add_work_items_with_sections

        Add WorkItems to TestPlan with Sections as TestSuites  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_analytics_get(self):
        """Test case for api_v2_test_plans_id_analytics_get

        Get analytics by TestPlan  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_autobalance_post(self):
        """Test case for api_v2_test_plans_id_autobalance_post

        Auto-balance for TestPlan with testers  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_configurations_get(self):
        """Test case for api_v2_test_plans_id_configurations_get

        Get TestPlan configurations  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_export_test_points_xlsx_post(self):
        """Test case for api_v2_test_plans_id_export_test_points_xlsx_post

        Export TestPoints from TestPlan in xls format  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_export_test_result_history_xlsx_post(self):
        """Test case for api_v2_test_plans_id_export_test_result_history_xlsx_post

        Export TestResults history from TestPlan in xls format  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_history_get(self):
        """Test case for api_v2_test_plans_id_history_get

        Get TestPlan history  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_links_get(self):
        """Test case for api_v2_test_plans_id_links_get

        Get Links of TestPlan  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_test_points_last_results_get(self):
        """Test case for api_v2_test_plans_id_test_points_last_results_get

        Get TestPoints with last result from TestPlan  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_test_points_reset_post(self):
        """Test case for api_v2_test_plans_id_test_points_reset_post

        Reset TestPoints status of TestPlan  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_test_runs_get(self):
        """Test case for api_v2_test_plans_id_test_runs_get

        Get TestRuns of TestPlan  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_test_runs_search_post(self):
        """Test case for api_v2_test_plans_id_test_runs_search_post

        Search TestRuns of TestPlan  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get(self):
        """Test case for api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get

        Get max modified date in TestRun for TestPlan  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_id_unlock_request_post(self):
        """Test case for api_v2_test_plans_id_unlock_request_post

        Send unlock TestPlan notification  # noqa: E501
        """
        pass

    def test_api_v2_test_plans_shorts_post(self):
        """Test case for api_v2_test_plans_shorts_post

        Get TestPlans short models by Project identifiers  # noqa: E501
        """
        pass

    def test_clone(self):
        """Test case for clone

        Clone TestPlan  # noqa: E501
        """
        pass

    def test_complete(self):
        """Test case for complete

        Complete TestPlan  # noqa: E501
        """
        pass

    def test_create_test_plan(self):
        """Test case for create_test_plan

        Create TestPlan  # noqa: E501
        """
        pass

    def test_delete_test_plan(self):
        """Test case for delete_test_plan

        Delete TestPlan  # noqa: E501
        """
        pass

    def test_get_test_plan_by_id(self):
        """Test case for get_test_plan_by_id

        Get TestPlan by Id  # noqa: E501
        """
        pass

    def test_get_test_suites_by_id(self):
        """Test case for get_test_suites_by_id

        Get TestSuites Tree By Id  # noqa: E501
        """
        pass

    def test_pause(self):
        """Test case for pause

        Pause TestPlan  # noqa: E501
        """
        pass

    def test_restore_test_plan(self):
        """Test case for restore_test_plan

        Restore TestPlan  # noqa: E501
        """
        pass

    def test_start(self):
        """Test case for start

        Start TestPlan  # noqa: E501
        """
        pass

    def test_update_test_plan(self):
        """Test case for update_test_plan

        Update TestPlan  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
