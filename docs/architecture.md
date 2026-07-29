# Architecture

```
                 main.py
                     │
          ┌──────────┴──────────┐
          │                     │
      config.py           services/
                               │
              ┌────────────────┴───────────────┐
              │                                │
         storage.py                     exporter.py
              │
              ▼
            core/
              │
      ┌───────┼────────┐
      │       │        │
 wallet.py history.py notifier.py
      │
      ▼
 monitor.py
```

## Components

### Wallet

Represents a monitored wallet and stores its current balance.

### Monitor

Coordinates wallet scanning and balance updates.

### History

Stores all detected balance changes.

### Notifier

Displays notifications for balance changes.

### Storage

Loads and saves wallet information in JSON format.

### Exporter

Exports collected history into CSV files.

### Utils

Contains reusable helper functions.
