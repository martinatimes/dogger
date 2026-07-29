import random

from core.wallet import Wallet
from core.history import History
from core.notifier import Notifier

from services.storage import WalletStorage


class WalletMonitor:

    def __init__(self, interval):

        self.interval = interval

        self.wallets = []

        self.history = History()

        self.notifier = Notifier()

    def load_wallets(self, filename):

        storage = WalletStorage(filename)

        self.wallets = storage.load()

    def scan(self):

        for wallet in self.wallets:

            old_balance = wallet.balance

            simulated_balance = round(

                wallet.balance + random.uniform(-15, 30),

                2,

            )

            wallet.update_balance(simulated_balance)

            self.history.add(

                wallet.address,

                old_balance,

                wallet.balance,

            )

            self.notifier.notify(

                wallet.address,

                wallet.balance - old_balance,

            )
