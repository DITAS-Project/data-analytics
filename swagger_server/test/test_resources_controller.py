# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.resources import Resources  # noqa: E501
from swagger_server.test import BaseTestCase


class TestResourcesController(BaseTestCase):
    """ResourcesController integration test stubs"""

    def test_current_usage(self):
        """Test case for current_usage

        Outputs the CPU percentage used by nodeId, the remaining free memory (MB) and the free space (GB) remaining on the storage cluster
        """
        response = self.client.open(
            '/data-analytics/resources/{infraId}/{nodeId}/usage/'.format(infraId='infraId_example', nodeId='nodeId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resources(self):
        """Test case for resources

        Outputs the CPU (cores) and memory (MB) capacity for nodeId and the capacity of the storage cluster (GB)
        """
        response = self.client.open(
            '/data-analytics/resources/{infraId}/{nodeId}/'.format(infraId='infraId_example', nodeId='nodeId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
