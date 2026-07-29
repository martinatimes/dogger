import unittest

from core.wallet import Wallet


class WalletTests(unittest.TestCase):

    def test_balance_update(self):

        wallet = Wallet(
            address="0x123",
            balance=100
        )

        diff = wallet.update_balance(135)

        self.assertEqual(diff, 35)
        self.assertEqual(wallet.balance, 135)

    def test_negative_difference(self):

        wallet = Wallet(
            address="0x123",
            balance=250
        )

        diff = wallet.update_balance(200)

        self.assertEqual(diff, -50)


if __name__ == "__main__":
    unittest.main()
