import unittest
from checks import check

class TestDiskUsage(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(check(30), "LOOKS FINE")
    def test_warning(self):
        self.assertEqual(check(76), "WARNING")
    def test_critical(self):
        self.assertEqual(check(89), "CRITICAL")
    def test_error(self):
        with self.assertRaises(ValueError):
            check(-1)
        with self.assertRaises(ValueError):
            check(101)
if __name__ == "__main__":
    unittest.main()
