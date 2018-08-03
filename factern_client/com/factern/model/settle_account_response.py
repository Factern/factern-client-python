# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class SettleAccountResponse():


    @staticmethod
    def compute_parent_updates():
        pass

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'settlement_id': 'str'
    }

    attribute_map = {
        'settlement_id': 'settlementId'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """SettleAccountResponse - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("SettleAccountResponse got unexpected argument '%s'" % k)

        self._settlement_id = None


        if "settlement_id" not in kwargs:
            raise ValueError("SettleAccountResponse missing required argument: settlement_id")
        self._settlement_id = kwargs["settlement_id"]


    @property
    def settlement_id(self):
        """Gets the settlement_id of this SettleAccountResponse.  # noqa: E501


        :return: The settlement_id of this SettleAccountResponse.  # noqa: E501
        :rtype: str
        """
        return self._settlement_id

    @settlement_id.setter
    def settlement_id(self, settlement_id):
        """Sets the settlement_id of this SettleAccountResponse.


        :param settlement_id: The settlement_id of this SettleAccountResponse.  # noqa: E501
        :type: str
        """
        if settlement_id is None:
            raise ValueError("Invalid value for `settlement_id`, must not be `None`")  # noqa: E501

        self._settlement_id = settlement_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SettleAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
