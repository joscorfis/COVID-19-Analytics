from django.test import TestCase
from main import queries
import unittest

class TestCases(TestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_basico(self):
        self.assertEqual(5,5)
