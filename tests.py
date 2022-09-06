# ----------------------------------------------------------------------
# - Name:       Brandon Schultz
# - Date:       4-16-22
# - Assignment: HW1 Blackbox Testing
# - Description: This file contains T/F unit tests for
# -  confirming valid credit card sequences.
# - References:
#  https://www.geeksforgeeks.org/program-credit-card-number-validation/
# ----------------------------------------------------------------------
# Test suite from std library:
import unittest
from credit_card_validator import credit_card_validator
# Class used for tests:
class testCase(unittest.TestCase):
    # ---------------------------------------
    # - Tests take the form of example below:                          |
    # ---------------------------------------
    # Generic explanation via comment...
    # def test11(self):
    #     self.assertFalse(credit_card_validator("...."))
    # ---------------------------------------------------
    # - Visa Test Cases:
    #  __________________________________________
    # | Visa Scope:| Prefix(es): 4 | Length: 16  |
    # |____________|_______________|_____________|
    # - Test 1: Checks for empty string
    # - Test 2: Required Length = 16, provided = 15
    # Visa val will be F.
    # - Test 3: Required Length = 16, provided = 16    
    # Visa val will be T.
    # ---------------------------------------------
    def test1(self):
        n = ''
        self.assertFalse(credit_card_validator(n))
    def test2(self):
        card_num = '413775306327881'
        self.assertFalse(credit_card_validator(card_num))        
    def test3(self):
        card_num = '4075407399425858'
        self.assertTrue(credit_card_validator(card_num))
    # -----------------------------------------------------
    # - American Express Cases:
    #  ____________________________________________
    # | AE Scope:| Prefix(es): 34,37 | Length: 15  |
    # |__________|___________________|_____________|
    # - Test 4: Required Length = 15, provided = 15
    # Sample val checks for incorrect check digit,
    # contains correct prefix + length values.
    # - Test 5: Required Length = 15, provided = 16
    # Should return false
    # ------------------------------------------------
    def test4(self):
        card_num = '370000000000001'
        self.assertFalse(credit_card_validator(card_num))
    def test5(self):
        card_num = '3700000000000001'
        self.assertFalse(credit_card_validator(card_num))
    # -----------------------------------------------------
    # - MasterCard Cases:
    # ____________________________________________________
    # | MC Scope:| Prefix(es): 51-55,2221-2720 | Length: 16|
    # |__________|_____________________________|___________|
    # - Test 6: Required Length = 16, provided = 16
    # Sample val checks for incorrect check digit
    # - Test 7: Required Length = 16, provided = 16
    # Sample val checks for incorrect prefix boundary val
    # ----------------------------------------------------
    def test6(self):
        card_num = '2221000000000001'
        self.assertFalse(credit_card_validator(card_num)) 
    def test7(self):
        card_num = '2720000000000005'
        self.assertTrue(credit_card_validator(card_num))    
if __name__ == '__main__':
    unittest.main(verbosity=2)
