**Package Sorter**

This is a small Python project that decides how to route packages in a warehouse.
The main code is in code.py.

**How it works**

A package is bulky if:

Its volume (width × height × length) is 1,000,000 cm³ or more, or

Any single dimension is 150 cm or more.

A package is heavy if its mass is 20 kg or more.

If it’s both bulky and heavy, it goes to REJECTED.

If it’s either bulky or heavy (but not both), it goes to SPECIAL.

Otherwise, it’s a STANDARD package.

**Function**

The main function is called sort and lives inside code.py.
It returns one of: STANDARD, SPECIAL, or REJECTED.



**Open a terminal and run:**

python code.py

You can edit the dimensions and mass in code.py to test with different packages.

**Tests**

Some simple test cases are included to check edge conditions:

Exact thresholds (150 cm, 20 kg, 1,000,000 cm³)

Just under thresholds

Zero-size packages

All tests currently pass ✅
