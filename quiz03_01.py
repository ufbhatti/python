# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 18:16:32 2025

@author: test
"""

import tkinter as tk
from tkinter import messagebox

def sort_numbers():
    try:
        # Get input from entry field
        numbers = list(map(int, entry.get().split()))

        # Check if exactly 10 numbers are entered
        if len(numbers) != 10:
            messagebox.showerror("Input Error", "Please enter exactly 10 numbers separated by spaces.")
            return

        # Sort the numbers
        numbers.sort()

        # Display sorted numbers
        result_label.config(text="Sorted Numbers: " + " ".join(map(str, numbers)))

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers separated by spaces.")

# Create GUI window
root = tk.Tk()
root.title("Number Sorter")
root.geometry("400x250")

# Add widgets
tk.Label(root, text="Enter 10 numbers separated by spaces:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

sort_button = tk.Button(root, text="Sort Numbers", command=sort_numbers, font=("Arial", 12), bg="blue", fg="white")
sort_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
result_label.pack(pady=10)

# Run GUI loop
root.mainloop()
