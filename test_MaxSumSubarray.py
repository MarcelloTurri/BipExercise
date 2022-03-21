import unittest
from MaxSumSubarray import getMaxContiguousSum

class MaxSumSubarray(unittest.TestCase):

    def test_with_one_number(self):

        self.assertEqual(getMaxContiguousSum([1]),(1, [1]))
        self.assertEqual(getMaxContiguousSum([0]),(0, [0]))
        self.assertEqual(getMaxContiguousSum([100]), (100, [100]))


    def test_with_all_positives(self):
        self.assertEqual(getMaxContiguousSum([1,2,3,4,5]),(15,[1,2,3,4,5]))

    def test_with_all_negatives(self):
        self.assertEqual(getMaxContiguousSum([-1, -2, -3, -4, -5]), (-1, [-1]))


    def test_with_positives_and_negatives(self):
        self.assertEqual(getMaxContiguousSum([-1,2,-3,1,2,3]), (6, [1, 2, 3]))
        self.assertEqual(getMaxContiguousSum([-3,10,-3,1,-19,1,2]),(10,[10]))
        self.assertEqual(getMaxContiguousSum([-1,-2,3,-7,9,-8,9]),(10, [9, -8, 9]))
        self.assertEqual(getMaxContiguousSum([0,4,-2,3,-4,0]),(5,[4,-2,3]))

    def test_with_noElement(self):
        self.assertEqual(getMaxContiguousSum([]),(0,[]))

    def test_type_error(self):
        self.assertRaises(TypeError, getMaxContiguousSum([True]))
        self.assertRaises(TypeError, getMaxContiguousSum(["1"]))
        self.assertRaises(TypeError, getMaxContiguousSum([{"key":2}]))

