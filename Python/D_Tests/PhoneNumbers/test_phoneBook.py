import unittest

from B_Logic.PhoneNumbers.PhoneBook import PhoneBook

class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phoneBook = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phoneBook.add("Bob", "12345")
        number = self.phoneBook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phoneBook.lookup("missing")

    #@unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phoneBook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phoneBook.add("Bob","12345")
        self.phoneBook.add("Susan","012345")
        self.assertTrue(self.phoneBook.is_consistent())

    def test_Inconsistent_with_duplicate_entries(self):
        self.phoneBook.add("Bob","12345")
        self.phoneBook.add("Susan","12345")
        self.assertFalse(self.phoneBook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phoneBook.add("Bob","12345")
        self.phoneBook.add("Susan","123")
        self.assertFalse(self.phoneBook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phoneBook.add("Sue", "12345")
        self.assertIn("Sue", self.phoneBook.get_names())
        self.assertIn("12345", self.phoneBook.get_numbers())
