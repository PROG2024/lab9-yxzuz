"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter

class SingletonTest(unittest.TestCase):
    """Tests of the counter class."""


    def test_singleton(self):
        c1 = Counter()
        c1.increment()
        self.assertEqual(2,c1.count)
        c2 = Counter()
        self.assertEqual(2,c2.count)

