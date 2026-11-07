# python-calculator

Minimal Python calculator (addition, subtraction, multiplication, division) with type hints, docstrings, and pytest unit tests.

This repository was created by Microsoft Foundry.

## Features

- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b) — raises ZeroDivisionError on division by zero

All functions accept numeric inputs and return floats. Type hints and docstrings are included.

## Installation

Clone the repository and install pytest for running tests:

```bash
git clone https://github.com/TrungTin101/python-calculator.git
cd python-calculator
python -m venv .venv
source .venv/bin/activate  # on Windows use `.venv\\Scripts\\activate`

pip install -U pip
pip install pytest
```

## Running tests

From the repository root run:

```bash
pytest -q
```

## Attribution

Repository created by Microsoft Foundry.
