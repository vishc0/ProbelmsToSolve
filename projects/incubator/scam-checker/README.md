# Scam Text & Email Checker

A straightforward tool to check whether a suspicious text message, email, or voicemail transcript is likely a scam.

corporations and busineses and common public today have resorted to inconvinience based behavior like spam calls , threatening call phishing, etc.. theremmust be tools developed so that a common man can take care fo the security aspects at no cost. this includes digital world and non digital world. 

## What It Does
When you or an aging relative get an alarming text:
1. **Plain Verdict:** Gives an immediate answer ("High Risk: Almost Certainly a Scam", "Suspicious", or "Low Risk").
2. **Red Flags:** Points out the exact tricks being used (e.g. artificial urgency, fake package delivery links, asking for payment in gift cards).
3. **Safe Next Steps:** Tells you clearly what to do (e.g. "Do not click the link. Log into your official bank app directly.").

## How to Run It
```bash
python3 src/scam_checker.py --text "USPS: Your parcel cannot be delivered. Click here to update your address within 12 hours: http://usps-track-now.info"
```

Run tests:
```bash
python3 tests/test_scam_checker.py
```
