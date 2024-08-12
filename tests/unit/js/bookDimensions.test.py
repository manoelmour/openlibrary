import unittest
from bookfunc import dimension_check

class Test(unittest.TestCase):
    def test_dimension_check_positives(self):
        self.assertTrue(dimension_check(1,2,3))

    def test_dimension_check_negatives_and_zero(self):
        with self.assertRaises(ValueError):
            dimension_check(-1,2,3)

        with self.assertRaises(ValueError):
                        dimension_check(1,0,3)

        with self.assertRaises(ValueError):
                        dimension_check(1,2,-3)

        with self.assertRaises(ValueError):
                        dimension_check(0,0,0)



if __name__ == '__name__':
    unittest.main()
