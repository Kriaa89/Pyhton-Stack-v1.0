# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
# steps 

def Countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list
# test the function
print(Countdown(5))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
# steps 
def print_and_return(numbers): # function that takes parameter number 
    print(numbers[0]) # print the first element of the list
    return numbers[1]  # return the second element of the list 
result = print_and_return([1,2]) # call the function and pass the list 
print(result)

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(list):
    return list[0] + len(list)
#test the function
result = first_plus_length([1,2,3,4,5])
print(result)

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    for i in range (0, len(list), 1):
        if list[i] > list[1]:
            new_list.append(list[i])
    print(len(new_list))
    return new_list

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def length_and_value(size, value):
    list = []
    for i in range(size):
        list.append(value)
    return list
# test the function
result = length_and_value(4,7)
print(result)