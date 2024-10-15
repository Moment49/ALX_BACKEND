import unittest


def add(x, y):
    """A function to add two numbers"""
    return x + y

class TestAdd(unittest.TestCase):
    """Test class for the numbers to be added"""

    def test_add_positive(self):
        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative(self):
        result = add(-5, 3)
        self.assertEqual(result, -2)

if __name__ == "__main__":
    unittest.main()