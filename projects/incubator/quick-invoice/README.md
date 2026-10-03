# Quick Invoice Generator

A simple tool for handymen, plumbers, landscapers, and solo tradespeople to turn rough notes or dictation into clean, professional invoices.

this is very important and useful tool for enterpreneurs to us for thier buisness needs, but at the same time they havet contribute and use this as an invoicing tool to be accurate.. so that it builds its own databases and give you the accyrate results. where ever its not established it will get you the ai research based result but as we go along this will build data and then use the accurate results. it shall use tools to accuately calculate the all costs like cost of travel and cost of delivery of the services or goods. 


## What It Does
When you finish a job with your hands covered in dust:
1. Type or speak a 15-second summary (e.g., *"Did the deck repair for Bob Miller. 3.5 hours labor at $60/hr. Replaced 4 cedar boards for $48.50 and screws for $12."*).
2. The tool breaks it down into labor, materials, and totals.
3. It prints a clean, formatted text invoice that you can immediately text or email to your customer.

## How to Run It
```bash
python3 src/quick_invoice.py --notes "Client: John Davis. Fixed kitchen sink drain. 2 hours labor at $75/hr. New PVC pipe and trap $32.40."
```

Run tests:
```bash
python3 tests/test_quick_invoice.py
```
