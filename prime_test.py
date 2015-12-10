"""unit testing """

import unittest
from prime import is_prime

class PrimeTestCase(unittest.TestCase):
    """test for the prime.py """
   
    def test_is_five_prime(self):
	"""is five is a prime """
        self.assertTrue(is_prime(5))

if __name__ == '__main__' :
    unittest.main()
