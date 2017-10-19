# coding: utf-8

"""
    BlueLens Index API

    This is a bl-api-index server.

    OpenAPI spec version: 0.0.1
    Contact: devops@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.image_api import ImageApi


class TestImageApi(unittest.TestCase):
    """ ImageApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.image_api.ImageApi()

    def tearDown(self):
        pass

    def test_add_image(self):
        """
        Test case for add_image

        Add a new image
        """
        pass

    def test_get_image_by_id(self):
        """
        Test case for get_image_by_id

        Get a image
        """
        pass


if __name__ == '__main__':
    unittest.main()
