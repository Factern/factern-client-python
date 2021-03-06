# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




parent_name = "CreateNamedRequest"
def get_parent():
    # Lazy importing of parent means that loading the classes happens
    # in the correct order.
    if get_parent.cache is None:
        parent_fname = "factern_client.com.factern.model.%s" % re.sub("([a-z])([A-Z])", "\\1_\\2", "CreateNamedRequest").lower()
        parent = importlib.import_module(parent_fname).CreateNamedRequest
        get_parent.cache = parent
    return get_parent.cache
get_parent.cache = None


class CreateGroupRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateGroupRequest.swagger_types.update(get_parent().swagger_types)
        CreateGroupRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'member_fact_type': 'str',
        'member_ids': 'list[str]'
    }

    attribute_map = {
        'member_fact_type': 'memberFactType',
        'member_ids': 'memberIds'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateGroupRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateGroupRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._member_fact_type = None
        self._member_ids = None


        if "member_fact_type" in kwargs:
            self.member_fact_type = kwargs["member_fact_type"]
        if "member_ids" not in kwargs:
            raise ValueError("CreateGroupRequest missing required argument: member_ids")
        self._member_ids = kwargs["member_ids"]


    @property
    def member_fact_type(self):
        """Gets the member_fact_type of this CreateGroupRequest.  # noqa: E501


        :return: The member_fact_type of this CreateGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._member_fact_type

    @member_fact_type.setter
    def member_fact_type(self, member_fact_type):
        """Sets the member_fact_type of this CreateGroupRequest.


        :param member_fact_type: The member_fact_type of this CreateGroupRequest.  # noqa: E501
        :type: str
        """

        self._member_fact_type = member_fact_type

    @property
    def member_ids(self):
        """Gets the member_ids of this CreateGroupRequest.  # noqa: E501


        :return: The member_ids of this CreateGroupRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_ids

    @member_ids.setter
    def member_ids(self, member_ids):
        """Sets the member_ids of this CreateGroupRequest.


        :param member_ids: The member_ids of this CreateGroupRequest.  # noqa: E501
        :type: list[str]
        """
        if member_ids is None:
            raise ValueError("Invalid value for `member_ids`, must not be `None`")  # noqa: E501

        self._member_ids = member_ids

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
        if not isinstance(other, CreateGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
