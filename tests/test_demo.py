import unittest

from demo import label, normalize


class TestBaseline(unittest.TestCase):
    def test_fixture_is_alive(self):
        self.assertTrue(True)


class TestLabel(unittest.TestCase):
    def test_labels_name(self):
        self.assertEqual(label("Ada"), "Hello, Ada!")

    def test_labels_empty_name_without_normalization(self):
        self.assertEqual(label(""), "Hello, !")

    def test_labels_padded_name(self):
        self.assertEqual(label(" Ada "), "Hello, Ada!")


class TestNormalize(unittest.TestCase):
    def test_strips_padded_name(self):
        self.assertEqual(normalize(" Ada "), "Ada")

    def test_keeps_unpadded_name(self):
        self.assertEqual(normalize("Ada"), "Ada")

    def test_keeps_empty_name(self):
        self.assertEqual(normalize(""), "")
