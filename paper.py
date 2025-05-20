# -*- coding: utf-8 -*-
"""
If- Condition 
#Q1

x=int(input("Enter Gained marks:"))

if x>90:
    print("A Grade")
else:
    if x>70:
        print("B Grade")
    else:
        if x>50:
            print("C Grade")
        else:
            print("FAIL")
            
#Qno 2

celsius= float(input("Enter temperature in Celsius: "))
print("You entered:", celsius, "°C")

if celsius>30:
    print("Hot")
else:
    if celsius>10:
        print("Warm")
    else:
        if celsius<10:
            print("Cold")
        else:
            print("Wron entry")
#Q no 3
num01=float(input("Enter Number 01:"))
num02=float(input("Enter Number 02:"))

if num01 > 0 and num02 > 0:
    total = num01 + num02
    print(f"Sum of {num01} and {num02} is: {total}")
else:
    if num01 < 0 and num02 < 0:
        total01 = num01 * num02
        print(f"Product of {num01} and {num02} is: {total01}")
    else:
            total02 = num01 - num02
            print(f"Difference of {num01} and {num02} is: {total02}")

 # Get input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Check the conditions
if a > 0 and b > 0:
    print("Sum:", a + b)
elif a < 0 and b < 0:
    print("Product:", a * b)
else:
    print("Difference:", a - b)
# For Loop

fruits = ["apple", "banana", "cherry", "date"] 

i=10
for x in fruits:
    print(x)

#Write a program to print the square of numbers from 1 to 5 using a for loop. 
#number =1,2,3,4,5
for i in range(6):
    print(i*i)
"""

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
for i in range(1,6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  # Move to the next line after each row
# While loop
#def guessing_game():
secret_number = 15

while True:
    guess = int(input("Enter your guess NUMBER: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it correctly.")
        break
print("invalid input")
'''
'''
#Write a program to calculate the sum of all elements in a list using a while loop. 
n= [5, 10, 15, 20, 25]  # Example list
total = 0
index = 0

while index < len(n):
    total += n[index]
    index += 1

print("Sum of all elements in the list:", total)
#remove duplicates from a list using while loop
original = [1, 2, 2, 3, 4, 4, 5, 1, 3]
unique = []
duplicates = []
i = 0

while i < len(original):
    item = original[i]
    if item not in unique:
        unique.append(item)
    elif item not in duplicates:
        duplicates.append(item)
    i += 1

print("List without duplicates:", unique)
print("Duplicate elements:", duplicates)
'''
'''
# lIST QUESTIONS
#1Write a program to sort a list of numbers in ascending order. 
numbers = [5, 2, 9, 1, 7, 3]
n = len(numbers)
i = 0

while i < n:
    j = 0
    while j < n - 1:
        if numbers[j] > numbers[j + 1]:
            # Swap values
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
        j += 1
    i += 1

print("Sorted list:", numbers)
#2Create a list of the squares of numbers from 1 to 10 using list comprehension. 
squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)
for i in range(1,11):
    
    k=i*i
    i+=1
    print(k)
#4Write a program to merge two lists into one without using + or extend() . 
list1 = [3, 1, 2, 3]
list2 = [4, 2, 5, 1]
merged = []

# Merge list1 without duplicates
for item in list1:
    if item not in merged:
        merged.append(item)

# Merge list2 without duplicates
for item in list2:
    if item not in merged:
        merged.append(item)

# Sort the merged list
i = 0
n = len(merged)
while i < n:
    j = 0
    while j < n - 1:
        if merged[j] > merged[j + 1]:
            merged[j], merged[j + 1] = merged[j + 1], merged[j]
        j += 1
    i += 1

print("Merged, unique, and sorted list:", merged)
'''


#4Take a list of numbers and double the value of each element. 
numbers = [1, 2, 3, 4, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

print("Original list:", numbers)
print("Doubled list:", doubled)

    
    