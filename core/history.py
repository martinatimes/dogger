from datetime import datetime


class History:

    def __init__(self):

        self.records = []

    def add(self, wallet, old_balance, new_balance):

        self.records.append({

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "wallet": wallet,

            "old_balance": round(old_balance, 2),

            "new_balance": round(new_balance, 2),

            "difference": round(new_balance - old_balance, 2)

        })

    def all(self):

        return self.records
