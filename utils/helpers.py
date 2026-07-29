from datetime import datetime


def current_timestamp():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_balance(balance):

    return f"{balance:.2f} USDC"


def percent_change(old, new):

    if old == 0:
        return 0.0

    return ((new - old) / old) * 100
