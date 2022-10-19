import unittest
from knapSack import dynamic, bruteforce, greedy, bruteforce_fractional
 
class TestBruteForce(unittest.TestCase):
 
    def setUp(self):
        self.p = [100, 50, 120, 60] 
        self.w = [3, 4, 2, 1] 
        self.m = 5
    

    def test_knapSack(self):
        self.assertEqual( bruteforce(self.W,self.wt, self.val), ('1010',220) )
    
    def test_bruteforce_fractional(self):
        self.assertEqual( bruteforce_fractional(self.p, self.w, self.m),  ([0.67, 0.0, 1.0, 1.0], 246.66666666666669) )
 
    def test_greedy(self):
        self.assertEqual( greedy(self.p, self.w, self.m), ([0.6666666666666666, 0, 1, 1], 246.66666666666666) )
 
    def test_dynamic(self):
        self.assertEqual( dynamic(self.p, self.w, self.m), ('1010', 220) )
 
if __name__ == "__main__":
    unittest.main()
