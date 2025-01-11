# Objectives:
# Avoid common mistakes of using functions
# Really understand how to use T-diagram to correctly predict and debug code

#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) # calling the fucntion number_of_food_groups and printing The result of the function
# result is 5 because the function returns 5 

#2
def number_of_military_branches(): # declaring a function called number_of_military_branches
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())  #  we have a error here inside the print because xe are caliing a function does not exist


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# he will return only 5 because the function will return 5 and then it will exist the function 

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# this function only will retrun 5 because the print satetment is after the return statement 

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes() 
print(x) 
# print 5 

#6
def add(b,c):
    print(b+c) # print 3 and 5
print(add(1,2) + add(2,3))# 3 and 5 and then we will have a error because the function does not retrun anything


#7
def concatenate(b,c):
    return str(b)+str(c) # retrun 25 as a string
print(concatenate(2,5)) # print 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7 # this line wiil not work because the function will retrun 10 and then leave the function 
print(number_of_oceans_or_fingers_or_continents())
# print 100 and then 10 because the function will return 10 because the value of b is greater than 10 so it will retrun 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c: 
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) 
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# 7
# 14 
# 21

#10
def addition(b,c): # 3,5
    return b+c
    return 10 
print(addition(3,5))
# 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# 500
# 500 
# 300
# 500

#12
b = 500
print(b) 
def foobar(): 
    b = 300
    print(b) 
    return b 
print(b) 
foobar()
print(b) 
# 500
# 500
# 300
# 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# 500
# 500
# 300
# 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# 1
# 3
# 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# 1
# 3
# 5 
# 10