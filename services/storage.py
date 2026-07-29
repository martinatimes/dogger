import json
from pathlib import Path

from core.wallet import Wallet


class WalletStorage:

    def __init__(self, filename: str):

        self.filename = Path(filename)

    def load(self):

        if not self.filename.exists():
            return []

        with open(self.filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        wallets = []

        for item in data:
            wallets.append(
                Wallet(
                    address=item["address"],
                    balance=item.get("balance", 0.0)
                )
            )

        return wallets

    def save(self, wallets):

        data = []

        for wallet in wallets:

            data.append({
                "address": wallet.address,
                "balance": wallet.balance
            })

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
