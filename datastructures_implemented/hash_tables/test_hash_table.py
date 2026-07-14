import unittest

from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.table = HashTable()

    def test_add_and_get(self):
        self.table.add("First", 1)

        self.assertEqual(self.table.get("First"), 1)

    def test_missing_key_returns_none(self):
        self.assertIsNone(self.table.get("Unknown"))

    def test_collision_handling(self):
        # "First" and "Third" have the same length -> same bucket
        self.table.add("First", 1)
        self.table.add("Third", 3)

        self.assertEqual(self.table.get("First"), 1)
        self.assertEqual(self.table.get("Third"), 3)

    def test_multiple_values(self):
        self.table.add("A", 100)
        self.table.add("B", 200)

        self.assertEqual(self.table.get("A"), 100)
        self.assertEqual(self.table.get("B"), 200)

    def test_iter(self):
        self.table.add("First", 1)
        self.table.add("Second", 2)

        items = list(self.table.iter())

        self.assertIn(("First", 1), items)
        self.assertIn(("Second", 2), items)


if __name__ == "__main__":
    unittest.main()