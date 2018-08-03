# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




class DeletedStatusItem():


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
        'deleted_item': 'DeletedItem',
        'status': 'int'
    }

    attribute_map = {
        'deleted_item': 'deletedItem',
        'status': 'status'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """DeletedStatusItem - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("DeletedStatusItem got unexpected argument '%s'" % k)

        self._deleted_item = None
        self._status = None


        if "deleted_item" not in kwargs:
            raise ValueError("DeletedStatusItem missing required argument: deleted_item")
        self._deleted_item = kwargs["deleted_item"]

        if "status" not in kwargs:
            raise ValueError("DeletedStatusItem missing required argument: status")
        self._status = kwargs["status"]


    @property
    def deleted_item(self):
        """Gets the deleted_item of this DeletedStatusItem.  # noqa: E501


        :return: The deleted_item of this DeletedStatusItem.  # noqa: E501
        :rtype: DeletedItem
        """
        return self._deleted_item

    @deleted_item.setter
    def deleted_item(self, deleted_item):
        """Sets the deleted_item of this DeletedStatusItem.


        :param deleted_item: The deleted_item of this DeletedStatusItem.  # noqa: E501
        :type: DeletedItem
        """
        if deleted_item is None:
            raise ValueError("Invalid value for `deleted_item`, must not be `None`")  # noqa: E501

        self._deleted_item = deleted_item

    @property
    def status(self):
        """Gets the status of this DeletedStatusItem.  # noqa: E501


        :return: The status of this DeletedStatusItem.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeletedStatusItem.


        :param status: The status of this DeletedStatusItem.  # noqa: E501
        :type: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, DeletedStatusItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
