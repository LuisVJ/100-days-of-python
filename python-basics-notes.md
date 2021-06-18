# Basics

## Print function

```python
print("Hello world")
```

* \n -> character for newline

```python
# concatenation:
print("Hello" + "world")
```

We can write comments with #

## input fuction

Prints a message to the console and waits for input.  
It will return the input and we can store it in a variable.

```python
name = input("What is your name? ")
print(name)
```

## len()

To show the length of a string we use the len function:

```python
print(len("Hello")) # 5
```

## Numbers

we can use "_" to separate thousands in numbers instead of commas or dots:
123_345_742

```python
print(231_241_124 + 233_325)
```

## Type conversion

```python
type(variable) # will tell us the data type of the variable
str(variable) # converts the data stored in variable into a string
float(variable) # converts into a float
int(variable) # converts into integer
```

## Number manipulation

```python
round(2.53535, 2) # rounds the number with 2 decimals
print(8//3) # floor division, returns integer 2 in this case.
```

## f-strings

```python
print(f"this is a formated string with a {variable}")
```

## Control Flow and Logical Operators

if/else satements:

```python
if condition:
    # Do this
elif condition 2:
    # Do this
else:
    # Do this instead
```

We can nest an if statements inside another if statement.  
we can also use the elif statement to check for several conditions.

comparison operators:

* ">"   -> greater than
* "<"   -> less than
* ">="  -> greater or equal
* "<="  -> less than or equal
* "=="  -> equal to
* "!="  -> not equal to

Logical operators:

* AND
* OR
* NOT

## Random module

---

We can create our own modules in separate files and then import tem with the keyword import

```python
# We need to import the module to be able to use it
import random

#create a random integer between start and end
a = random.randint(start, end)
# create a random floating point between 0 and 1(excluded)
f = random.random()
```

check [documentation](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences) for more functions

## Lists

---

```python
# declare a list
fruits = ["apple", "orange", "banana"]
```

Lists are ordered  
we can use negative indexes to acces the values:  

* fruits[-1] will return banana

```python
# add items to the list
fruits.append("pear")
```

More methods in the [Documentation](https://docs.python.org/3/tutorial/datastructures.html)

## Loops

---

* For Loop

```python
for item in items:
    # Code

# We can use the range() function to iterate
for i in range(a, b)
    # code
```

The range won't include b. We can also specify the step as a third parameter

* While loop

```python
while condition:
    # code
```

## Fuctions

---

```python
# Declaring a function
def my_function():
    #code

# Calling the function
my_function():
```

* Keyword arguments:

```python
def my_function(name, location):
    #code

# Calling the function with keyword arguments:
my_function(location="here", name="pepe")
```

In this case the order of the arguments doesn't matter because we are using the specific names of the arguments.

### Docstrings

we can add documentation to our functions:

```python
def my_function():
    """ Documentation of our function explaning what it does, how ...."""

    # code
```

## Dictionaries

---

 ```python
my_dictionary = {
    "key1" = "value1",
    "key2" = "value2",
}
# To retrieve the information:
print(my_dictionary["key2"])

# To add new key value pairs. Also to redefine values of existing keys:

my_dictionary["newKey"] = "newValue"
 ```

Looping throug dictionaries:

```python
for a in my_dictionary:
    # a is the keys of the dictionary
    my_dictionary[a] # the value of said key
```

## Managing Files

---

```python
# Open a file to a variable
file = open("my_file.txt")
# reading the file
contents = file.read()
# close the file
file.close() # to save resources
```

A diferent way to open a file:

```python
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
# It will close the file atomatically
```

We can open the file in diferent modes:

```python
# Opening in write mode
with open("my_file.txt", mode="w") as file:
    file.write("New text.") 
    # This will overwrite the contents
    mode="a"
    # this mode will add the new text to the existing content

```

## Pandas

---

```python
import pandas

data = pandas.read_csv("filename") 

# loop through rows of a data frame
for (index, row) in data_frame.iterrows():
    print(row.column_name)
```

## List comprehension

---

```python
list = [1, 2 ,3]
new_list = [new_item for item in list if condition]
# The condition is optional
```

We can also use comprehension with dictionaries

```python
new_dict = {new_key:new_value for item in list}

new_dict = {new_key:new_value for (key,value) in dict.items()}
# we can also have conditions
# example:

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor"]

students_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student, score) in students_scores if score >= 60}

```

## Errors and exceptions

---

* try: something that might cause an exception.
* except: Do this if there was an exception.
* else: Do this if there were no exceptions.
* finally: Do this no matter what happens.

```python
try:
    file = open("my_file.txt")
except FileNotFoundError: # It's best practice to specify the type of error we are trying to catch
    print("There was an error, file not found")
    # We could create a new file to handle this error
    file = open("my_file.txt", "w")
except KeyError as error_message:
    # Handle this type of error, but not the previous one
    print(f"The key {error_message} doesn't exist")
else:
    # It will execute if the there is no exceptions
    content = file.read()
    print(content)
finally:
    # It will always execute. Is not often used
    file.close()
    print("File closed")
```

* raise: it allows us to raise our own exceptions

```python
raise TypeError("This is an error that I made up")
############## Example #############

height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metters.")

bmi = weight / height ** 2
print(bmi)
```
