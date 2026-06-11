import tkinter as tk
from tkinter import messagebox

def calculate_discount():
    """Calculates the discount and updates the screen."""
    try:
        # Step 1: Grab the data from the text boxes
        price = float(entry_price.get())
        discount = float(entry_discount.get())
        quantity = int(entry_quantity.get())

        # Step 2: Make sure the numbers make sense (no negative prices!)
        if price < 0 or discount < 0 or quantity <= 0:
            messagebox.showwarning("Warning", "Please enter valid positive numbers.")
            return

        # Step 3: Do the math
        subtotal = price * quantity
        discount_amount = subtotal * (discount / 100)
        final_price = subtotal - discount_amount

        # Step 4: Show the final result on the screen
        result_label.config(text=f"Final Price: Rp {final_price:,.2f}")

    except ValueError:
        # Step 5: Catch the error if the user types letters instead of numbers
        messagebox.showerror("Error", "Oops! Please enter numbers only.")

# ================= USER INTERFACE =================
window = tk.Tk()
window.title("Discount Calculator")
window.geometry("350x300")

# Title
tk.Label(window, text="Discount Calculator", font=("Arial", 14, "bold")).pack(pady=10)

# Price Input
tk.Label(window, text="Original Price").pack()
entry_price = tk.Entry(window)
entry_price.pack()

# Discount Input
tk.Label(window, text="Discount (%)").pack()
entry_discount = tk.Entry(window)
entry_discount.pack()

# Quantity Input
tk.Label(window, text="Quantity").pack()
entry_quantity = tk.Entry(window)
entry_quantity.pack()

# Calculate Button
tk.Button(window, text="Calculate", command=calculate_discount).pack(pady=10)

# Result Label
result_label = tk.Label(window, text="Final Price: Rp 0.00", font=("Arial", 11))
result_label.pack(pady=10)

window.mainloop()
