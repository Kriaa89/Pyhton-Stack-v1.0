# Now, the Assignment:
# Note: Avoid using class keywords like int, str, list, and dict as variable/parameter names.
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
# test the change
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0] ['last_name'] = 'Bryant'
# test the change 
print(students)
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
# test the change 
print(sports_directory)
# Change the value 20 in z to 30
z [0]['y'] = 30

# 2.Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in 
# the list and prints each key and the associated value. For example, given the following list:
def iterateDictionary(students):
    for key in students:
        print(key)
# test the function 
iterateDictionary(students)
# bonus to get them to appear exactly as below!)
def iterateDictionary(students):
    for keys in students:
        print(f"last_name - {keys['last_name']}  first_name - {keys['first_name']}")
# test the function
iterateDictionary(students)


# 3.Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
key_name = 'first_name'
def iterateDictionary2(key_name, students):
    for keys in students:
        print(keys[key_name])
# test the function 
iterateDictionary2('first_name', students)