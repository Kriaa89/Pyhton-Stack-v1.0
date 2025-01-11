num1 = 42 # varaible declartion type int
num2 = 2.3 # varaible declartion type float
boolean = True  # variable declartion type boolean
string = 'Hello World' # variable declartion type string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable decalration type list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # varaible declaration type dictionary
fruit = ('blueberry', 'strawberry', 'banana') # varaible declaration type tuple
print(type(fruit)) # print type of varaible fruit 
print(pizza_toppings[1]) # print index 1 of pizza_toppings list is Sausage
pizza_toppings.append('Mushrooms') # append Mushrooms to pizza_toppings list
print(person['name']) # print value of key name is John
person['name'] = 'George' # change value of key name to George
person['eye_color'] = 'blue' # add key eye_color with value blue
print(fruit[2]) # print index 2 of friut tuple is banana


# conditional statements
if num1 > 45: # if num1 is greater than 45 
    print("It's greater") 
else:
    print("It's lower") 
# result print It's lower because num1 is less than 45 


if len(string) < 5: #  if length of string is less thn 5 
    print("It's a short word!") 
elif len(string) > 15: #  if length of string is greater  thn 15
    print("It's a long word!")
else:
    print("Just right!")
# result Just right! because length of string is 11

for x in range(5): # for loop from 0 to 4
    print(x) 
for x in range(2,5): # for loop from 2 to 4
    print(x)
for x in range(2,10,3): #for loop from 2 to 9 with steps of 3
    print(x)
x = 0 # variable x is 0 
while(x < 5): # while loop x is less than 5 
    print(x) # print x is 0
    x += 1 # increament x by 1

pizza_toppings.pop() # remove last element of pizza_toppings  
pizza_toppings.pop(1) # remove element at index 1 of pizza_toppings is sausage

print(person) # print person dictioanry
person.pop('eye_color') # remove key eye_color from disctonary 
print(person) # print person dictionary {'name': 'John','location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings: # for loop to go throught pizza topping list 
    if topping == 'Pepperoni':
        continue # continue to next iteration
    print('After 1st if statement') 
    if topping == 'Olives': # if topping is olives
        break #break the loop

def print_hello_ten_times():  # function called print_hello_ten_times
    for num in range(10): #for loop from 0 to 9 
        print('Hello') # print Hello 
print_hello_ten_times() # call the function tp print hello 10 times

def print_hello_x_times(x): # function called print_hello_x_times with parameter x 
    for num in range(x): 
        print('Hello')
print_hello_x_times(4) # call the function to print hello 4 times




def print_hello_x_or_ten_times(x = 10): # function called print_hello_x_or_ten_times with default parameter x = 10
    for num in range(x): # for loop to print hello x times
        print('Hello') 

print_hello_x_or_ten_times() # clall the function to print hello 10 times
print_hello_x_or_ten_times(4) # call the function to print hello 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)