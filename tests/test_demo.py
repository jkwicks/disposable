import unittest

from demo import label


class TestBaseline(unittest.TestCase):
    def test_fixture_is_alive(self):
        self.assertTrue(True)


class TestLabel(unittest.TestCase):
    def test_labels_name(self):
        self.assertEqual(label("Ada"), "Hello, Ada!")

    def test_labels_empty_name_without_normalization(self):
        self.assertEqual(label(""), "Hello, !")
