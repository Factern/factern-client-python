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


class CreateWatchRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateWatchRequest.swagger_types.update(get_parent().swagger_types)
        CreateWatchRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'filter_id': 'str',
        'target_node_id': 'str',
        'watch_interface_id': 'str'
    }

    attribute_map = {
        'filter_id': 'filterId',
        'target_node_id': 'targetNodeId',
        'watch_interface_id': 'watchInterfaceId'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateWatchRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateWatchRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._filter_id = None
        self._target_node_id = None
        self._watch_interface_id = None


        if "filter_id" in kwargs:
            self.filter_id = kwargs["filter_id"]
        if "target_node_id" not in kwargs:
            raise ValueError("CreateWatchRequest missing required argument: target_node_id")
        self._target_node_id = kwargs["target_node_id"]

        if "watch_interface_id" in kwargs:
            self.watch_interface_id = kwargs["watch_interface_id"]

    @property
    def filter_id(self):
        """Gets the filter_id of this CreateWatchRequest.  # noqa: E501


        :return: The filter_id of this CreateWatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._filter_id

    @filter_id.setter
    def filter_id(self, filter_id):
        """Sets the filter_id of this CreateWatchRequest.


        :param filter_id: The filter_id of this CreateWatchRequest.  # noqa: E501
        :type: str
        """

        self._filter_id = filter_id

    @property
    def target_node_id(self):
        """Gets the target_node_id of this CreateWatchRequest.  # noqa: E501


        :return: The target_node_id of this CreateWatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_node_id

    @target_node_id.setter
    def target_node_id(self, target_node_id):
        """Sets the target_node_id of this CreateWatchRequest.


        :param target_node_id: The target_node_id of this CreateWatchRequest.  # noqa: E501
        :type: str
        """
        if target_node_id is None:
            raise ValueError("Invalid value for `target_node_id`, must not be `None`")  # noqa: E501

        self._target_node_id = target_node_id

    @property
    def watch_interface_id(self):
        """Gets the watch_interface_id of this CreateWatchRequest.  # noqa: E501


        :return: The watch_interface_id of this CreateWatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._watch_interface_id

    @watch_interface_id.setter
    def watch_interface_id(self, watch_interface_id):
        """Sets the watch_interface_id of this CreateWatchRequest.


        :param watch_interface_id: The watch_interface_id of this CreateWatchRequest.  # noqa: E501
        :type: str
        """

        self._watch_interface_id = watch_interface_id

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
        if not isinstance(other, CreateWatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
