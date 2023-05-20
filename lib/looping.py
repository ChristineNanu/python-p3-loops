#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

    

def square_integers(numbers):
    squared_numbers = []
    for num in numbers:
        if isinstance(num, int):
            squared_numbers.append(num ** 2)
    return squared_numbers

    
    
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
 
 

