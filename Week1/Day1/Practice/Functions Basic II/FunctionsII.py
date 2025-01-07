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