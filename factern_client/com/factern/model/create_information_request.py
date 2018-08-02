# coding: utf-8

"""
    Factern API
"""


import pprint
import re  # noqa: F401

import six
import importlib




parent_name = "CreateChildRequest"
def get_parent():
    # Lazy importing of parent means that loading the classes happens
    # in the correct order.
    if get_parent.cache is None:
        parent_fname = "factern_client.com.factern.model.%s" % re.sub("([a-z])([A-Z])", "\\1_\\2", "CreateChildRequest").lower()
        parent = importlib.import_module(parent_fname).CreateChildRequest
        get_parent.cache = parent
    return get_parent.cache
get_parent.cache = None


class CreateInformationRequest(get_parent()):

    @staticmethod
    def get_parent():
        return get_parent()

    @staticmethod
    def compute_parent_updates():
        pass

        get_parent().compute_parent_updates()

        CreateInformationRequest.swagger_types.update(get_parent().swagger_types)
        CreateInformationRequest.attribute_map.update(get_parent().attribute_map)


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data': 'str',
        'field_id': 'str',
        'storage_id': 'str'
    }

    attribute_map = {
        'data': 'data',
        'field_id': 'fieldId',
        'storage_id': 'storageId'
    }

    def __init__(self, **kwargs):  # noqa: E501
        """CreateInformationRequest - a model defined in Swagger"""  # noqa: E501
        self.compute_parent_updates()
        for k in kwargs:
            if k not in self.swagger_types:
                raise ValueError("CreateInformationRequest got unexpected argument '%s'" % k)
        get_parent().__init__(self, **kwargs)

        self._data = None
        self._field_id = None
        self._storage_id = None


        if "data" not in kwargs:
            raise ValueError("CreateInformationRequest missing required argument: data")
        self._data = kwargs["data"]

        if "field_id" not in kwargs:
            raise ValueError("CreateInformationRequest missing required argument: field_id")
        self._field_id = kwargs["field_id"]

        if "storage_id" in kwargs:
            self.storage_id = kwargs["storage_id"]

    @property
    def data(self):
        """Gets the data of this CreateInformationRequest.  # noqa: E501


        :return: The data of this CreateInformationRequest.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CreateInformationRequest.


        :param data: The data of this CreateInformationRequest.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def field_id(self):
        """Gets the field_id of this CreateInformationRequest.  # noqa: E501


        :return: The field_id of this CreateInformationRequest.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this CreateInformationRequest.


        :param field_id: The field_id of this CreateInformationRequest.  # noqa: E501
        :type: str
        """
        if field_id is None:
            raise ValueError("Invalid value for `field_id`, must not be `None`")  # noqa: E501

        self._field_id = field_id

    @property
    def storage_id(self):
        """Gets the storage_id of this CreateInformationRequest.  # noqa: E501


        :return: The storage_id of this CreateInformationRequest.  # noqa: E501
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this CreateInformationRequest.


        :param storage_id: The storage_id of this CreateInformationRequest.  # noqa: E501
        :type: str
        """

        self._storage_id = storage_id

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
        if not isinstance(other, CreateInformationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
