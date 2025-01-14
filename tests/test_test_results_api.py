"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import testit_api_client
from testit_api_client.api.test_results_api import TestResultsApi  # noqa: E501


class TestTestResultsApi(unittest.TestCase):
    """TestResultsApi unit test stubs"""

    def setUp(self):
        self.api = TestResultsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v2_test_results_id_aggregated_get(self):
        """Test case for api_v2_test_results_id_aggregated_get

        """
        pass

    def test_api_v2_test_results_id_attachments_attachment_id_put(self):
        """Test case for api_v2_test_results_id_attachments_attachment_id_put

        """
        pass

    def test_api_v2_test_results_id_attachments_info_get(self):
        """Test case for api_v2_test_results_id_attachments_info_get

        """
        pass

    def test_api_v2_test_results_id_external_projects_external_project_id_defect_post(self):
        """Test case for api_v2_test_results_id_external_projects_external_project_id_defect_post

        """
        pass

    def test_api_v2_test_results_id_external_projects_external_project_id_form_get(self):
        """Test case for api_v2_test_results_id_external_projects_external_project_id_form_get

        """
        pass

    def test_api_v2_test_results_id_get(self):
        """Test case for api_v2_test_results_id_get

        """
        pass

    def test_api_v2_test_results_id_link_requests_post(self):
        """Test case for api_v2_test_results_id_link_requests_post

        """
        pass

    def test_api_v2_test_results_id_put(self):
        """Test case for api_v2_test_results_id_put

        """
        pass

    def test_api_v2_test_results_link_requests_link_request_id_use_post(self):
        """Test case for api_v2_test_results_link_requests_link_request_id_use_post

        """
        pass

    def test_create_attachment(self):
        """Test case for create_attachment

        Upload and link attachment to TestResult  # noqa: E501
        """
        pass

    def test_delete_attachment(self):
        """Test case for delete_attachment

        Remove attachment and unlink from TestResult  # noqa: E501
        """
        pass

    def test_download_attachment(self):
        """Test case for download_attachment

        Get attachment of TestResult  # noqa: E501
        """
        pass

    def test_get_attachment(self):
        """Test case for get_attachment

        Get Metadata of TestResult's attachment  # noqa: E501
        """
        pass

    def test_get_attachments(self):
        """Test case for get_attachments

        Get all attachments of TestResult  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
