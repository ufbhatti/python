# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 18:10:22 2025

@author: test
"""


numbers = list(map(int, input("Enter 10 numbers separated by spaces: ").split()))

# Check if the user entered exactly 10 numbers
if len(numbers) != 10:
    print("Please enter exactly 10 numbers.")
else:
    # Sort the numbers
    numbers.sort()
    
    # Print the sorted list
    print("Sorted numbers:", numbers)
