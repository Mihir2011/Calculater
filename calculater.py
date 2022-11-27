import os

os.system('cls')
print("What do you want do? ")
print("1. additon ")
print("2. subtraction ")
print("3. multiplication ")
calculation = input("4. division ")

if calculation == "1": 
    os.system('cls')
    add_number1 = input("Type your first number ")
    add_number2 = input("Type your second number ")
    sum = int(add_number1) + int(add_number2)
    print("The answer is", sum)
    
if calculation == "2": 
    os.system('cls')
    sub_number1 = input("Type your first number ")
    sub_number2 = input("Type your second number ")
    sub = int(sub_number1) - int(sub_number2)
    print("The answer is", sub)
    
if calculation == "3": 
    os.system('cls')
    mul_number1 = input("Type your first number ")
    mul_number2 = input("Type your second number ")
    mul = int(mul_number1) * int(mul_number2)
    print("The answer is", mul)

if calculation == "4": 
    os.system('cls')
    div_number1 = input("Type your first number ")
    div_number2 = input("Type your second number ")
    div = int(div_number1) / int(div_number2)
    print("The answer is", div)