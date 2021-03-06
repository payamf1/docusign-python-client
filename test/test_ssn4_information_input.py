# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import docusign_esign
from docusign_esign.rest import ApiException
from docusign_esign.models.ssn4_information_input import Ssn4InformationInput


class TestSsn4InformationInput(unittest.TestCase):
    """ Ssn4InformationInput unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSsn4InformationInput(self):
        """
        Test Ssn4InformationInput
        """
        model = docusign_esign.models.ssn4_information_input.Ssn4InformationInput()


if __name__ == '__main__':
    unittest.main()
