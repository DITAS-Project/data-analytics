# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MetricResInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, operation_id: str=None, name: str=None, value: float=None, unit: str=None, timestamp: datetime=None, appendix: str=None):  # noqa: E501
        """MetricResInner - a model defined in Swagger

        :param operation_id: The operation_id of this MetricResInner.  # noqa: E501
        :type operation_id: str
        :param name: The name of this MetricResInner.  # noqa: E501
        :type name: str
        :param value: The value of this MetricResInner.  # noqa: E501
        :type value: float
        :param unit: The unit of this MetricResInner.  # noqa: E501
        :type unit: str
        :param timestamp: The timestamp of this MetricResInner.  # noqa: E501
        :type timestamp: datetime
        :param appendix: The appendix of this MetricResInner.  # noqa: E501
        :type appendix: str
        """
        self.swagger_types = {
            'operation_id': str,
            'name': str,
            'value': float,
            'unit': str,
            'timestamp': datetime,
            'appendix': str
        }

        self.attribute_map = {
            'operation_id': 'operationID',
            'name': 'name',
            'value': 'value',
            'unit': 'unit',
            'timestamp': 'timestamp',
            'appendix': 'appendix'
        }

        self._operation_id = operation_id
        self._name = name
        self._value = value
        self._unit = unit
        self._timestamp = timestamp
        self._appendix = appendix

    @classmethod
    def from_dict(cls, dikt) -> 'MetricResInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The metricRes_inner of this MetricResInner.  # noqa: E501
        :rtype: MetricResInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def operation_id(self) -> str:
        """Gets the operation_id of this MetricResInner.


        :return: The operation_id of this MetricResInner.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id: str):
        """Sets the operation_id of this MetricResInner.


        :param operation_id: The operation_id of this MetricResInner.
        :type operation_id: str
        """

        self._operation_id = operation_id

    @property
    def name(self) -> str:
        """Gets the name of this MetricResInner.


        :return: The name of this MetricResInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this MetricResInner.


        :param name: The name of this MetricResInner.
        :type name: str
        """

        self._name = name

    @property
    def value(self) -> float:
        """Gets the value of this MetricResInner.


        :return: The value of this MetricResInner.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """Sets the value of this MetricResInner.


        :param value: The value of this MetricResInner.
        :type value: float
        """

        self._value = value

    @property
    def unit(self) -> str:
        """Gets the unit of this MetricResInner.


        :return: The unit of this MetricResInner.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit: str):
        """Sets the unit of this MetricResInner.


        :param unit: The unit of this MetricResInner.
        :type unit: str
        """

        self._unit = unit

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this MetricResInner.


        :return: The timestamp of this MetricResInner.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this MetricResInner.


        :param timestamp: The timestamp of this MetricResInner.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def appendix(self) -> str:
        """Gets the appendix of this MetricResInner.


        :return: The appendix of this MetricResInner.
        :rtype: str
        """
        return self._appendix

    @appendix.setter
    def appendix(self, appendix: str):
        """Sets the appendix of this MetricResInner.


        :param appendix: The appendix of this MetricResInner.
        :type appendix: str
        """

        self._appendix = appendix
