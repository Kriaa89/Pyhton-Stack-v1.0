# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
# steps 

def Countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
        return list
    

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
# steps 
def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]