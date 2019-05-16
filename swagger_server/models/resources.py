# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Resources(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, cpu: int=None, mem: int=None, storage: int=None):  # noqa: E501
        """Resources - a model defined in Swagger

        :param cpu: The cpu of this Resources.  # noqa: E501
        :type cpu: int
        :param mem: The mem of this Resources.  # noqa: E501
        :type mem: int
        :param storage: The storage of this Resources.  # noqa: E501
        :type storage: int
        """
        self.swagger_types = {
            'cpu': int,
            'mem': int,
            'storage': int
        }

        self.attribute_map = {
            'cpu': 'cpu',
            'mem': 'mem',
            'storage': 'storage'
        }

        self._cpu = cpu
        self._mem = mem
        self._storage = storage

    @classmethod
    def from_dict(cls, dikt) -> 'Resources':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Resources of this Resources.  # noqa: E501
        :rtype: Resources
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cpu(self) -> int:
        """Gets the cpu of this Resources.


        :return: The cpu of this Resources.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu: int):
        """Sets the cpu of this Resources.


        :param cpu: The cpu of this Resources.
        :type cpu: int
        """

        self._cpu = cpu

    @property
    def mem(self) -> int:
        """Gets the mem of this Resources.


        :return: The mem of this Resources.
        :rtype: int
        """
        return self._mem

    @mem.setter
    def mem(self, mem: int):
        """Sets the mem of this Resources.


        :param mem: The mem of this Resources.
        :type mem: int
        """

        self._mem = mem

    @property
    def storage(self) -> int:
        """Gets the storage of this Resources.


        :return: The storage of this Resources.
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage: int):
        """Sets the storage of this Resources.


        :param storage: The storage of this Resources.
        :type storage: int
        """

        self._storage = storage
