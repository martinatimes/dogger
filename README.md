# Circle Wallet Monitor

Circle Wallet Monitor is a lightweight Python application for monitoring multiple USDC wallets.

The application keeps track of balance changes, stores history, generates notifications and exports activity into CSV reports.

---

## Features

- Monitor multiple wallets
- Track USDC balance changes
- Store balance history
- Console notifications
- CSV export
- Modular architecture
- JSON wallet storage
- Simple configuration

---

## Project Structure

```
circle-wallet-monitor/

core/
services/
utils/
tests/
docs/
data/
output/
```

---

## Example

Wallet

```
0x4A7D31B2F9C71B5AAE1D0001
```

Previous Balance

```
1200.50
```

Current Balance

```
1225.75
```

Output

```
[+] Wallet updated

Change:
+25.25 USDC
```

---

## Installation

```bash
git clone https://github.com/yourname/circle-wallet-monitor.git

cd circle-wallet-monitor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

## Future Improvements

- Circle API integration
- Web dashboard
- Email notifications
- Telegram bot
- SQLite storage
- Historical analytics
- Portfolio statistics

---

## License

MIT
