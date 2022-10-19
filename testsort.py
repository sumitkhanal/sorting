import unittest
from mergesort import mergesort
from insertionsort import insertionsort
 
class SortingTestCase(unittest.TestCase):
 
    def test_insertion_sort(self):
        input1 = [2, 5, 4, 3, 1]
        Output1 = [1, 2, 3, 4, 5]
        input2 = [54,26,93,17,77,31,44,55,20]
        Output2 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
 
        insertionsort(input1)
        insertionsort(input2)
 
        self.assertListEqual(input1, Output1)
        self.assertEqual(len(input1), 5)
        self.assertListEqual(input2, Output2)
        self.assertEqual(len(input2), 9)
 
    def test_merge_sort(self):
        input1 = [2, 5, 4, 3, 1]
        Output1 = [1, 2, 3, 4, 5]
        input2 = [54,26,93,17,77,31,44,55,20]
        Output2 = [17, 20, 26, 31, 44, 54, 55, 77, 93]
 
        mergesort(input1)
        mergesort(input2)
 
        self.assertListEqual(input1, Output1)
        self.assertEqual(len(input1), 5)
        self.assertListEqual(input2, Output2)
        self.assertEqual(len(input2), 9)
 
 
 
if __name__ == '__main__':
    unittest.main()
