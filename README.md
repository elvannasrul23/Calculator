# Discount Calculator - Python Tkinter

A simple Graphical User Interface (GUI) application built with Python's standard `tkinter` library. This project is designed as an introductory lesson for students learning GUI development, input validation, and basic event handling in Python.

## Overview
This application simulates a basic point-of-sale (POS) calculation. Users can input an item's price, the discount percentage, and the quantity. The program processes the inputs, validates them to prevent mathematical errors, and outputs the final calculated price.

## Learning Objectives
This project is structured to help students understand:
* **UI Fundamentals:** Using standard widgets such as `Label`, `Entry`, and `Button`.
* **Data Type Conversion:** Retrieving string inputs from a GUI and converting them into `float` and `int` for calculation.
* **Error Handling:** Implementing `try...except` blocks to handle `ValueError` and gracefully manage incorrect user inputs (e.g., typing letters instead of numbers).
* **Control Flow:** Using basic `if/else` conditions to prevent invalid logic, such as negative pricing.

## Features
* Clean, top-to-bottom procedural code structure (ideal for beginners).
* Input validation for negative numbers and zero-quantity.
* Built-in error catching with UI message boxes (`tkinter.messagebox`).
* Uses Python's built-in libraries (no third-party dependencies required).

## Installation and Usage

1. Ensure [Python 3.x](https://www.python.org/downloads/) is installed on your system.
2. Clone this repository:
   git clone [https://github.com/yourusername/discount-calculator.git](https://github.com/yourusername/discount-calculator.git)
3. Navigate to the project directory:
   cd discount-calculator
4. Run the script:
   python discount_calculator.py
