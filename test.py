import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):
    def test_to_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertEqual(to_upper("HeLlO"), "HELLO")
        self.assertEqual(to_upper("123"), "123")
        self.assertEqual(to_upper(""), "") 

class TestToLower(unittest.TestCase):
    def test_to_lower(self):
        self.assertEqual(to_lower("HELLO"), "hello")
        self.assertEqual(to_lower("HeLlO"), "hello")
        self.assertEqual(to_lower("123"), "123")
        self.assertEqual(to_lower(""), "")

# class TestCapitalize(unittest.TestCase):
#     def test_capitalize(self):
#         self.assertEqual(capitalize("hello"), "Hello")
#         self.assertEqual(capitalize("HeLlO"), "Hello")
#         self.assertEqual(capitalize("123"), "123")
#         self.assertEqual(capitalize(""), "")

if __name__ == '__main__':
    unittest.main()
