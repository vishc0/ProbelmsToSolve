# Subscription & Bill Checker

A simple, private tool to find recurring subscriptions and sneaky price increases from your downloaded bank or credit card statements.

a human assitance to avoid harmful habits and utilize human capabilties to useful means. purely based on previous habits. this is one example, seocnd example is to cultivate good habits. a habit choose and follower, rather than following people. 

## What It Does
1. Reads a downloaded bank or credit card statement (CSV format).
2. Automatically identifies charges that repeat every month (streaming, gym, software, utilities).
3. Flags sneaky price increases (e.g., your internet went from $50.00 to $65.00).
4. Calculates the total amount leaving your bank account on autopilot every month.

*100% Private:* Runs entirely on your own computer. Your financial data is never sent to the internet or any server.

## How to Run It
```bash
python3 src/subscription_checker.py --csv sample_statement.csv
```

Run tests:
```bash
python3 tests/test_subscription_checker.py
```
