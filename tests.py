"""
----------------------------------------------------------------------
# - Name:       Brandon Schultz
# - Date:       4-16-22
# - Assignment: HW2 Improving Testing Coverage
# - Description: This file applies white box testing techniques that
#   achieve 100% Branch and Conditional Coverage in the testing of the
#   contrived_func function:
#  __________________________________________________________
   | def contrived_func(val):
   | # This function serves no logical purpose
   | # DO NOT try to make sense of it!
   | # Just make sure your tests cover everything requested
   | # val is a numerical value
   | if val < 150 and val > 100:
   |     return True
   | elif val * 5 < 361 and val / 2 < 24:
   |     if val == 6:
   |         return False
   |     else:
   |         return True
   | elif (val > 75 or val / 8 < 10) and val**val % 5 == 0:
   |     return True
   | else:
   |    return False
   |__________________________________________________________
#  
#  - Program is graded via secondary sw and produces print statements 
#   when any of 12 conditional combinations is triggered. There are 12  
#   such triggers labled c1-12. Note that submitted file also includes
#   tests for non successful triggering of c1-12 attempts, though submission
#   requires seven or fewer tests. 
#        
# - References:
#   https://www.geeksforgeeks.org/program-credit-card-number-validation/
#   https://www.geeksforgeeks.org/software-engineering-white-box-testing/
#   https://www.geeksforgeeks.org/differences-between-black-box-testing-vs-white-box-testing/
#   https://en.wikipedia.org/wiki/Obfuscation#White_box_cryptography=
#   
----------------------------------------------------------------------
"""


import unittest
from contrived_func import contrived_func


class BranchAndConditionalCovergaeTests(unittest.TestCase):
    # linting why
    def test1(self):
    	self.assertFalse(contrived_func(6))
    	
    # linting why
    def test2(self):
        self.assertTrue(contrived_func(75))   
          
    # linting why       
    def test3(self):
        self.assertTrue(contrived_func(47))
        
    # linting why       
    def test4(self):
        self.assertFalse(contrived_func(49))
        
    # linting why
    def test5(self):
        self.assertTrue(contrived_func(80))
  
     # linting why
    def test6(self):
        self.assertFalse(contrived_func(151))
        
    # linting why
    def test7(self):
        self.assertTrue(contrived_func(101))


if __name__ == '__main__':
    unittest.main()
