import unittest
from atm import ATM
class TestATM(unittest.TestCase):

    def setUp(self):
        self.atm = ATM(initial_balance=50000, default_pin="0000")

    def test_check_balance(self):
        # Checking initial balance
        self.assertEqual(self.atm.balance, 50000)

    def test_withdraw_valid_amount(self):
        # Test withdrawing a valid amount
        result = self.atm.withdraw(1000)
        self.assertEqual(result, "Withdrawal successful! Your new balance is $49000.00")
        self.assertEqual(self.atm.balance, 49000)

    def test_withdraw_invalid_amount(self):
        # Test withdrawing a negative amount
        result = self.atm.withdraw(-500)
        self.assertEqual(result, "Please enter a valid amount to withdraw.")
        # Test withdrawing zero
        result = self.atm.withdraw(0)
        self.assertEqual(result, "Please enter a valid amount to withdraw.")

    def test_withdraw_insufficient_funds(self):
        # Test withdrawing more than the balance
        result = self.atm.withdraw(60000)
        self.assertEqual(result, "Insufficient funds. Unable to process the withdrawal.")
        self.assertEqual(self.atm.balance, 50000)  # Balance should remain unchanged

    def test_deposit_valid_amount(self):
        # Test depositing a valid amount
        result = self.atm.deposit(500)
        self.assertEqual(result, "Deposit successful! Your new balance is 50500.00 SDG")
        self.assertEqual(self.atm.balance, 50500)

    def test_deposit_invalid_amount(self):
        # Test depositing a negative amount
        result = self.atm.deposit(-200)
        self.assertEqual(result, "Please enter a valid deposit amount.")
        # Test depositing zero
        result = self.atm.deposit(0)
        self.assertEqual(result, "Please enter a valid deposit amount.")

    def test_verify_pin_correct(self):
        # Test verifying the correct PIN
        self.assertTrue(self.atm.verify_pin("0000"))

    def test_verify_pin_incorrect(self):
        # Test verifying an incorrect PIN
        self.assertFalse(self.atm.verify_pin("1234"))

    def test_change_pin_success(self):
        # Test changing PIN with correct current PIN and matching new PINs
        result = self.atm.change_pin("0000", "1234", "1234")
        self.assertEqual(result, "PIN changed successfully.")
        self.assertTrue(self.atm.verify_pin("1234"))

    def test_change_pin_incorrect_old_pin(self):
        # Test changing PIN with an incorrect current PIN
        result = self.atm.change_pin("1111", "1234", "1234")
        self.assertEqual(result, "Incorrect current PIN.")
        self.assertTrue(self.atm.verify_pin("0000"))  # PIN should remain unchanged

    def test_change_pin_non_matching_new_pins(self):
        # Test changing PIN with non-matching new PINs
        result = self.atm.change_pin("0000", "1234", "4321")
        self.assertEqual(result, "The new PIN entries do not match.")
        self.assertTrue(self.atm.verify_pin("0000"))  # PIN should remain unchanged

    def test_change_pin_too_short(self):
        # Test changing PIN with a new PIN that's too short
        result = self.atm.change_pin("0000", "123", "123")
        self.assertEqual(result, "PIN should be at least 4 digits long.")
        self.assertTrue(self.atm.verify_pin("0000"))  # PIN should remain unchanged

if __name__ == '__main__':
    unittest.main()
