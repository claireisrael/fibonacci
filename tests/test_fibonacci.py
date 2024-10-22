import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from fibonacci_module import fibonacci  # Adjust this line according to your actual file name

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        result = fibonacci(0)
        self.assertEqual(result, 0)

    def test_fibonacci_1(self):
        result = fibonacci(1)
        self.assertEqual(result, 1)

    def test_fibonacci_2(self):
        result = fibonacci(2)
        self.assertEqual(result, 1)

    def test_fibonacci_3(self):
        result = fibonacci(3)
        self.assertEqual(result, 2)

    def test_fibonacci_4(self):
        result = fibonacci(4)
        self.assertEqual(result, 3)

if __name__ == '__main__':  # Use double underscores
    unittest.main()
