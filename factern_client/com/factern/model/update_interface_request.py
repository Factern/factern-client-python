# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




parent_name = "BaseRequest"
def get_parent():
    # Lazy importing of parent means that loading the classes happens
    # in the correct order.
    if get_parent.cache is None:
        parent_fname = "factern_client.com.factern.model.%s" % re.sub("([a-z])([A-Z])", "\\1_\\2", "BaseRequest").lower()
        parent = importlib.import_module(parent_fname).BaseRequest
        get_parent.cache = parent
    return get_parent.cache
get_parent.cache = None


class UpdateInterfaceRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        UpdateInterfaceRequest.swagger_types.update(get_parent().swagger_types)
        UpdateInterfaceRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'add_data': 'ApiEndpoint',
        'delete_data': 'ApiEndpoint',
        'get_data': 'ApiEndpoint',
        'node_id': 'str'
    }

    attribute_map = {
        'add_data': 'addData',
        'delete_data': 'deleteData',
        'get_data': 'getData',
        'node_id': 'nodeId'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """UpdateInterfaceRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("UpdateInterfaceRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._add_data = None
        self._delete_data = None
        self._get_data = None
        self._node_id = None


        if "add_data" in kwargs:
            self.add_data = kwargs["add_data"]
        if "delete_data" in kwargs:
            self.delete_data = kwargs["delete_data"]
        if "get_data" in kwargs:
            self.get_data = kwargs["get_data"]
        if "node_id" not in kwargs:
            raise ValueError("UpdateInterfaceRequest missing required argument: node_id")
        self._node_id = kwargs["node_id"]


    @property
    def add_data(self):
        """Gets the add_data of this UpdateInterfaceRequest.  # noqa: E501


        :return: The add_data of this UpdateInterfaceRequest.  # noqa: E501
        :rtype: ApiEndpoint
        """
        return self._add_data

    @add_data.setter
    def add_data(self, add_data):
        """Sets the add_data of this UpdateInterfaceRequest.


        :param add_data: The add_data of this UpdateInterfaceRequest.  # noqa: E501
        :type: ApiEndpoint
        """

        self._add_data = add_data

    @property
    def delete_data(self):
        """Gets the delete_data of this UpdateInterfaceRequest.  # noqa: E501


        :return: The delete_data of this UpdateInterfaceRequest.  # noqa: E501
        :rtype: ApiEndpoint
        """
        return self._delete_data

    @delete_data.setter
    def delete_data(self, delete_data):
        """Sets the delete_data of this UpdateInterfaceRequest.


        :param delete_data: The delete_data of this UpdateInterfaceRequest.  # noqa: E501
        :type: ApiEndpoint
        """

        self._delete_data = delete_data

    @property
    def get_data(self):
        """Gets the get_data of this UpdateInterfaceRequest.  # noqa: E501


        :return: The get_data of this UpdateInterfaceRequest.  # noqa: E501
        :rtype: ApiEndpoint
        """
        return self._get_data

    @get_data.setter
    def get_data(self, get_data):
        """Sets the get_data of this UpdateInterfaceRequest.


        :param get_data: The get_data of this UpdateInterfaceRequest.  # noqa: E501
        :type: ApiEndpoint
        """

        self._get_data = get_data

    @property
    def node_id(self):
        """Gets the node_id of this UpdateInterfaceRequest.  # noqa: E501


        :return: The node_id of this UpdateInterfaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this UpdateInterfaceRequest.


        :param node_id: The node_id of this UpdateInterfaceRequest.  # noqa: E501
        :type: str
        """
        if node_id is None:
            raise ValueError("Invalid value for `node_id`, must not be `None`")  # noqa: E501

        self._node_id = node_id

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
        if not isinstance(other, UpdateInterfaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
