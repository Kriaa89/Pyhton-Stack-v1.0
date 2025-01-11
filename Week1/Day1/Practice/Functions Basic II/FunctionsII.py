# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]
# steps 
# create a function with a name countdown and give it a parameter num
# create a varaibale list to store in it the result 
# and then create for loop start from the num and tacke step back -1 and stop in 0 we gonna use -1 
# after the for loop we need to append the each number in list varaible so we gonna use append 
# and the return the result 

def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result
# test the function
print(countdown(5))


# Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
# steps
# we gonna create function called print_and_return and give it two parameter number
# and then print the first element in the lsit using index 0
# after that return the second element in the list using index 1

def print_and_return(number):
    print(number[0])
    return number[1]
# test the function
print(print_and_return([1,2]))

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in 
# the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
# steps
# create a function first_plus_length and give it a parameter lst
# then we gonna declare a variable first_value and store in it the first element in the list using index 0
# the we gonna declare a varaible name lenght and store in it the lenght of the lsit using len()
# the we gonna return the sum of the first_value and the the lenght of list 
def first_plus_length(lst):
    first_value = lst[0]
    length = len(lst)
    return first_value + length
# test the function 
result = first_plus_length([1,2,3,4,6])
print(result)

# Values Greater than Second - Write a function that accepts a list 
# and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values 
# this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
# steps 
# create a function called values_greater_than_second and give it a parameter lst
# after that we gonna check if the lenght of the list is less than the 2 we gonna return False 
# then we gonna declare a  varaible called result to store in the element are biger than the second element in the list using index 1
# then we gonna use for loop to go throught the list and check all the element there are biger than the second element in the list
# after that we gonna append the element are boiger than the second element in lst in the result varaible
#then we gonna print the the lenght of the result varaible 
# and then we gonna return the result varaible 

def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    result = []
    for i in range(len(lst)):
        if lst[i] > lst[1]:
            result.append(lst[i])
            print(len(result))
        return result
# test the function
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))


# This Length, That Value - Write a function that accepts two integers 
# as parameters: size and value. The function should create and return a list whose length is equal to the given size, 
# and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size, value):
    result = []
    for i in range(size):
        result.append(value)
    return result
# test the function 
print(length_and_value(4,7))