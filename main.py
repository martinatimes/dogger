from config import DEFAULT_SCAN_INTERVAL
from core.monitor import WalletMonitor
from services.exporter import CSVExporter


def main():

    monitor = WalletMonitor(DEFAULT_SCAN_INTERVAL)

    monitor.load_wallets("data/wallets.json")

    monitor.scan()

    exporter = CSVExporter()

    exporter.export(
        monitor.history.records,
        "output/history.csv",
    )

    print("\nMonitoring finished.")


if __name__ == "__main__":
    main()
