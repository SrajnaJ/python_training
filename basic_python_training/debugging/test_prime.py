import unittest
from prime_check import is_prime

class TestPrimeFunction(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))

    def test_large_prime(self):
        self.assertTrue(is_prime(101))

    def test_large_non_prime(self):
        self.assertFalse(is_prime(100))

if __name__ == '__main__':
    unittest.main()
