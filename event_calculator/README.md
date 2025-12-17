# DJ 2TUFF Event Pricing Calculator (Python CLI)

A command-line tool that generates **instant DJ event quotes** with **validated user input** and **exportable quote files**. Built to model real service-business pricing logic (rates, travel fees, discounts) and produce a shareable quote in seconds.

## Features

* **Package menu (1–6)** for common event types (Party, Club, Wedding, Corporate, Game, Festival)
* **Strong input validation** (no crashes from invalid input)

  * menu selection validation
  * numeric validation for hours/distance
  * yes/no validation for discounts and file export
* **Travel fee calculation** based on distance
* **Discount support** (Sigma / FSU / friend)
* **Quote export** to a `.txt` file (client name + date in filename)

## How It Works (Pricing Rules)

* **Hourly rate** depends on selected package
* **Travel fee**

  * 0–10 miles: $0
  * 11–25 miles: $20
  * 26+ miles: $40
* **Discount**: 20% off subtotal when eligible

## Requirements

* Python 3.x

## Run

From the project folder:

```bash
python3 dj_calculator.py
```

## Example Usage

1. Select a package (1–6)
2. Enter hours + distance
3. Choose discount eligibility
4. (Optional) Generate a quote file

Example output:

```
===== FINAL QUOTE =====
Event Type: Corporate
Hours: 3.0
Hourly Rate: $120.00/hr
Travel Fee: $20.00
Subtotal: $380.00
Discount: -$76.00
TOTAL: $304.00
========================
✅ Saved: quote_Acme_Corp_12-20-2025.txt
```

## Project Highlights (Why This Matters)

This project demonstrates:

* Clean CLI design
* Defensive programming & input validation
* Data modeling via dictionaries (package → rate mapping)
* Real-world business logic implementation
* File output for practical usability

## Future Improvements

* Save quotes as **PDF** in addition to `.txt`
* Add **minimum booking fee** logic
* Add **tax / deposit** support
* Add a `--quick-quote` mode using command-line arguments (argparse)


