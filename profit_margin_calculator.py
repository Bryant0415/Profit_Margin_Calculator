import tkinter as tk
from tkinter import ttk

def calculate_GPM():
    try: 
        # Get user inputs
        net_sales = float(Net_Sales.get())
        cogs = float(Cost_Of_Goods.get())

        # Prevent division by zero
        if net_sales == 0:
            result_label.config(text="❌ Error: Net Sales cannot be zero!", fg="red")
            return
        
        # Prevent negative values
        if net_sales < 0 or cogs < 0:
            result_label.config(text="❌ Error: Values cannot be negative!", fg="red")
            return

        # Perform calculations
        GPM = ((net_sales - cogs) / net_sales) * 100

        # Display results
        result_label.config(
            text = f"✅ Net Sales: ${net_sales:,.2f}\n"
                   f"🛒 Cost of Goods: ${cogs:,.2f}\n"
                   f"📊 Gross Profit Margin: {GPM:,.2f}%\n",
            fg="green"
        )
    except ValueError:
        result_label.config(text="❌ Please enter valid numeric values! Do not include commas or currency symbols.", fg="red")

# Create main application window
root = tk.Tk()
root.title("Gross Profit Margin Calculator")
root.geometry("500x400")
root.resizable(False, False)

# Title Label
title_label = tk.Label(root, text="Gross Profit Margin Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Net Sales Input
tk.Label(root, text="Enter Total Net Sales:", font=("Arial", 12)).pack(pady=5)
Net_Sales = tk.Entry(root, font=("Arial", 12))
Net_Sales.pack()

# COGS Input
tk.Label(root, text="Enter Total Cost of Goods:", font=("Arial", 12)).pack(pady=5)
Cost_Of_Goods = tk.Entry(root, font=("Arial", 12))
Cost_Of_Goods.pack()

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Gross Profit Margin", command=calculate_GPM, bg="blue", fg="white", font=("Arial", 12, "bold"))
calculate_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()
