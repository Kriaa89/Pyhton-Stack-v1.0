This section contains basic exercises to understand and practice Python for loops. Below are the exercises included in the loop.py file:

Basic - Print all integers from 0 to 150

Python
for i in range(151):
    print(i)
Explanation: This loop prints all integers from 0 to 150.
Helpful Link: Python range() Function
Multiples of Five - Print all the multiples of 5 from 5 to 1,000

Python
for i in range(5, 1001, 5):
    print(i)
Explanation: This loop prints all multiples of 5 from 5 to 1000.
Helpful Link: Python For Loops
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"

Python
for i in range(1, 101):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo")
Explanation: This loop prints integers from 1 to 100. If the integer is divisible by 5, it prints "Coding". If it is divisible by 10, it prints "Coding Dojo".
Helpful Link: Python Conditional Statements
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum

Python
sum = 0
for i in range(500001):
    if i % 2 != 0:
        sum += i
        print(sum)
Explanation: This loop adds all odd integers from 0 to 500,000 and prints the running total.
Helpful Link: Python Arithmetic Operators
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours

Python
for i in range(2018, 0, -4):
    print(i)
Explanation: This loop prints positive numbers starting at 2018, counting down by fours.
Helpful Link: Python range() Function
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult

Python
lowNum = 2
highNum = 9 
mult  = 3 
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
Explanation: This loop prints integers from lowNum to highNum that are multiples of mult.
Helpful Link: Python Variables
Steps for Learning
Understand the Basics: Start with understanding basic Python syntax and how loops work.
Python For Beginners
Practice: Use the examples provided in the loop.py file to practice writing and understanding loops.
Explore More: Check out additional resources and documentation to deepen your understanding.
Python Official Documentation
W3Schools Python Tutorial
