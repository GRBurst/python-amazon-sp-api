# coding: utf-8

"""
    Selling Partner API for Feeds

    The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.  # noqa: E501

    OpenAPI spec version: 2020-09-04
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CreateFeedDocumentResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'payload': 'CreateFeedDocumentResult',
        'errors': 'ErrorList'
    }

    attribute_map = {
        'payload': 'payload',
        'errors': 'errors'
    }

    def __init__(self, payload=None, errors=None):  # noqa: E501
        """CreateFeedDocumentResponse - a model defined in Swagger"""  # noqa: E501
        self._payload = None
        self._errors = None
        self.discriminator = None
        if payload is not None:
            self.payload = payload
        if errors is not None:
            self.errors = errors

    @property
    def payload(self):
        """Gets the payload of this CreateFeedDocumentResponse.  # noqa: E501


        :return: The payload of this CreateFeedDocumentResponse.  # noqa: E501
        :rtype: CreateFeedDocumentResult
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this CreateFeedDocumentResponse.


        :param payload: The payload of this CreateFeedDocumentResponse.  # noqa: E501
        :type: CreateFeedDocumentResult
        """

        self._payload = payload

    @property
    def errors(self):
        """Gets the errors of this CreateFeedDocumentResponse.  # noqa: E501


        :return: The errors of this CreateFeedDocumentResponse.  # noqa: E501
        :rtype: ErrorList
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CreateFeedDocumentResponse.


        :param errors: The errors of this CreateFeedDocumentResponse.  # noqa: E501
        :type: ErrorList
        """

        self._errors = errors

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
        if issubclass(CreateFeedDocumentResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateFeedDocumentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
