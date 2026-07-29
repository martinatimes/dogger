from dataclasses import dataclass


@dataclass
class Wallet:

    address: str
    balance: float = 0.0

    def update_balance(self, new_balance: float):

        previous = self.balance

        self.balance = round(new_balance, 2)

        return round(self.balance - previous, 2)
