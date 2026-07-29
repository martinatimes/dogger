class Notifier:

    def notify(self, wallet, difference):

        if difference > 0:

            print(
                f"[+] {wallet} received {difference:.2f} USDC"
            )

        elif difference < 0:

            print(
                f"[-] {wallet} spent {abs(difference):.2f} USDC"
            )

        else:

            print(
                f"[=] {wallet} unchanged"
            )
