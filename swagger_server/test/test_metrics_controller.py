# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.metric_res import MetricRes  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMetricsController(BaseTestCase):
    """MetricsController integration test stubs"""

    def test_getmetrics(self):
        """Test case for getmetrics

        
        """
        query_string = [('operationID', 'operationID_example'),
                        ('name', 'name_example'),
                        ('startTime', '2013-10-20T19:20:30+01:00'),
                        ('endTime', '2013-10-20T19:20:30+01:00')]
        response = self.client.open(
            '/data-analytics/meter/{infraId}/'.format(infraId='infraId_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
