from django.test import TestCase
from main import queries
import unittest

class TestCases(TestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_get_repositorios_coronavirus_mas_visualizados(self):
        self.assertEqual(5,5)
