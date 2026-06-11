# Discount Calculator — Python Tkinter

A beginner-friendly GUI application built with Python's built-in `tkinter` library, simulating a simple point-of-sale (POS) discount calculator. No third-party packages required.

---

## Screenshot

> *(Add your screenshot here after running the app)*
> `screenshot.png`

---

## Overview

Users enter an item's original price, a discount percentage, and the quantity. The app validates all inputs, calculates the final total, and displays the result — all through a clean graphical interface.

This project is structured as an **introductory lesson** for students learning Python GUI development.

---

## Learning Objectives

By completing this project, students will understand:

- **UI Fundamentals** — Building layouts with `Label`, `Entry`, and `Button` widgets.
- **Data Type Conversion** — Parsing string inputs from a GUI into `float` and `int` for arithmetic.
- **Error Handling** — Using `try...except` blocks to catch `ValueError` and display user-friendly error messages via `tkinter.messagebox`.
- **Control Flow** — Applying `if/else` conditions to prevent invalid logic (e.g., negative prices, zero quantity).
- **Event Handling** — Binding button clicks to callback functions.

---

## Features

- Clean top-to-bottom procedural code structure (ideal for beginners)
- Input validation for negative numbers and zero quantity
- Friendly error dialogs using `tkinter.messagebox`
- No external dependencies — runs on any standard Python 3 installation

---

## Project Structure

```
discount-calculator/
├── discount_calculator.py   # Main application script
└── README.md
```

---

## Requirements

- Python 3.x — [Download here](https://www.python.org/downloads/)
- `tkinter` is included with Python by default (no extra install needed)

> **Linux users:** If `tkinter` is missing, install it with:
> ```bash
> sudo apt install python3-tk
> ```

---

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/elvannasrul23/Calculator.git
   ```

2. **Navigate to the project folder:**
   ```bash
   cd Calculator
   ```

3. **Run the application:**
   ```bash
   python discount_calculator.py
   ```

---

## How It Works

| Input Field        | Description                          | Valid Range     |
|--------------------|--------------------------------------|-----------------|
| Price (Rp)         | Original price of the item           | > 0             |
| Discount (%)       | Discount percentage to apply         | 0 – 100         |
| Quantity           | Number of items being purchased      | ≥ 1 (integer)   |

**Formula used:**

```
discounted_price = price * (1 - discount / 100)
total            = discounted_price * quantity
```

---

## Example

| Input         | Value   |
|---------------|---------|
| Price         | 150,000 |
| Discount      | 20%     |
| Quantity      | 3       |
| **Total**     | **360,000** |

---

## Error Handling

The app handles the following invalid inputs gracefully:

- Non-numeric input (e.g., typing letters in a number field)
- Negative price or discount
- Discount greater than 100%
- Quantity less than 1 or non-integer quantity

All errors trigger a `messagebox.showerror()` dialog with a clear message — no crashes.

## License

This project is released under the [MIT License](LICENSE). Free to use and modify for educational purposes.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

*Built as a learning project for Python GUI programming students.*
