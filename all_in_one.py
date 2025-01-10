


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# list comprehention: a quick way to create lists/ sets / dictionary in python.
# instead of looping or appending to a bunch of items to lists 

my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

# insted of doing this another way is list comprehension which is faster and clear
# formate of list comprehention
# my_list = [parameter for parameter in iterable]
# print(my_list)

my_list = [char or char in 'hello']
my_list2 = [num for num in range (0,100)]
my_list3 = [num*2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]
print(my_list4)


#------------------------------------------------------------------------------------

# is v/s ==

# == : it is checking types of both sides 
# in this we check the value
print(True == 1)
print(''==1)
print([]==1)
print(10 == 10.0)
print([] == [])

# is : a keyword in python, checks the location in memory where this value is stored is the same
# in 'is' you are checking for exact equality
print(True is 1)  # True is not 1 , True == True
print('1' is 1)    # string 1 is not int 1
print([] is 1)      # empty arrat is not list 
print(10 is  10)   # True
print([] is [])

a = [1,2,3]
b = [1,2,3]
print (a is b)
# False, because list are created are stored in different locations in memory



#------------------------------------------------------------------------

# for loop:

# one of the most powerful feature of the python 
# Iterable: It is an object or collection that can be iterated over 
for item in 'bucket':   
    print(item) 
    print(item)
    print(item)
print(item)    # t prints 4 times but other letters are only 3 times

for item in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item,x)
        
# iterable: list, dictionary, tuple, set, string 
# iterated: one by one check each item in the collection 


user = {
        'name':'rutuja',
        'age':20,
        'can_swim': False
        }
for item in user:
    print(item)

# print the keys of the dictionary
#o/p:
    '''
    name
    age
    can_swim
    '''
#+++++++++++++++++++++++++++++++++++++++++++++++++++
    
for item in user.items():
    print(item)

#o/p: displays the key-value pair in a tuple.
    
'''
('name', 'rutuja')
('age', 20)
('can_swim', False)
'''

#++++++++++++++++++++++++++++++++++++
for item in user.values():
    print(item)
    
#o/p: prints the values of each key:
    '''
    rutuja
    20
    False
    '''
#+++++++++++++++++++++++++++++++++++++++++++

for item in user.keys():
    print(item) 
#o/p: Iterated over keys 
    '''
    name
    age
    can_swim
    '''

#++++++++++++++++++++++++++++++++++++++++++++

for item in user.items():
    key, value = item;
    print(key, value)
    
#o/p: using tuple unpacking 
    '''
    name rutuja
    age 20
    can_swim False
    '''
    
#+++++++++++++++++++++++++++++++++++++++++++

# Another shorthand way using for loop:

for key, value in user.items():
    print(key,value)
    
#o/p:
    '''
    name rutuja
    age 20
    can_swim False
    '''
    
#-------------------------------------------------------------------------

# counter

my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0
for item in my_list:
    counter = counter + item
print(counter)


#______________________________________________________________________________



# range(): return an object that produces a sequence of integers from start to stop
# range creates a special kind of object that we can iterate over.

print(range(100))
# range(0, 100)

for number in range(0,10):
    print(number)  
# print 0 to 9

for _ in range(0,10,2):
    print(_)
#o/p:
    '''
    0
    2
    4
    6
    8
    '''

for _ in range(0,10,-1):
    print(_)
# no output

for _ in range(10,0,-1):
    print(_)
# o/p: 10 to 1

for _ in range(10,0,-2):
    print(_)
# o/p: 10 8 6 4 2

for _ in range(2):
    print(list(range(10)))
#o/p:
    '''
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
    
    
#------------------------------------------------------------------------------

# enumerate(): it going to take iterable object and gives index count and item of that index
for i,char in enumerate('helloooo'):
    print(i,char)
#o/p:
    '''
    0 h
    1 e
    2 l
    3 l
    4 o
    5 o
    6 o
    7 o
    '''
    
for i,char in enumerate((1,2,3)):
    print(i,char)
#o/p:
    '''
    0 1
    1 2
    2 3
    '''
for i,char in enumerate([1,2,3]):
    print(i,char)
#o/p:
    '''
    0 1
    1 2
    2 3
    '''
    
for i,char in enumerate(list(range(100))):
    if char==50:
        print(f'index of 50 is:{i}')
#o/p: index of 50 is:50


#--------------------------------------------------------------------------

# while loop:  very flexible but for loops are simpler
i = 0
while i <50:
    print(i)    # only this much code then there will be infinite loop
    i = i + 1   # or i += 1
# o/p: 0 to 49 will be print 
else:
    print('done with all the work')
# o/p: 0 to 49 will be print ... done with all the work


#-----------------------------------------------------------------------

#for iterating over iterable objects 'for' loops are great
my_list=[1,2,3]
for item in [1,2,3]:
    print(item)


# but when you are not sure how many times you want loop over something, 
# when you are not sure that how long its take for looping then go for 'while' loop
i = 0
while i <len([1,2,3]):
    print(my_list[i])
    i += 1
    
while True:
    input('say something: ')
    break

# say something : hi
# if we don't break it, while loop keep on sending say something many time i.e. infinite times

while True:
    response = input('say something: ')
    if(response == 'bye'):
        break
#o/p: until we say bye it will loop again
    '''
    say something: hi
    say something: hi
    say something: hi
    say something: bye
    '''
    
    
#-------------------------------------------------------------------------

# break, continue
# break: breaks out of the current enclosing loop (break the loop)
# continue: whatever happen continue from the top of the enclosing loop
# pass : passes to next line
my_list = [1,2,3]
for item in my_list:
    print(item)
    continue


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue

# o/p: 1 2 3 


my_list = [1,2,3]
for item in my_list:
    # thinking about it
    pass        # it is the placeholder whenever we are not sure about next step use 'pass'

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue

#------------------------------------------------------------------------

# GUI : Graphical User Interface
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]
#1. Iterate over picture
for row in picture:
    for pixel in row:
        if (pixel == 1):
            print("*", end='')  # if 0 -> print ''
        else:
            print(" ", end='')  # if 1 -> print *
    print('')    # need a new line after every row
    
    
#------------------------------------------------------------------------

#what is good code?
# clean code
# readability
# predictability
# DRY : Do Not Repeat Yourself


#------------------------------------------------------------------------

# Find duplicate values 

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        duplicate.append(value)
print(duplicate)

# o/p: ['b', 'b', 'n', 'n'] 
    
#======================================================
  
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)
print(duplicate)

# o/p: ['b', 'n']


#------------------------------------------------------------------------

# Functions:  after creating function we have to call it for the use.
    # functions supports DRY property 
    # we can defined once and use anywhere in the program
    # def funct_name : created memory for that function
def say_hello():
    print("hello") 
say_hello()     

#o/p: hello


# power of the function 

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]
# defined the funcation name as tree and can call may time when it is needed
def tree():
    for row in picture:
        for pixel in row:
            if (pixel == 1):
                print("*", end='')  # if 0 -> print ''
            else:
                print(" ", end='')  # if 1 -> print *
        print('')   
tree()
tree()

print(tree)
#o/p: <function tree at 0x000001D5396833A0>  
      #function named tree is at this location


#----------------------------------------------------------------------------

# Argument v/s Parameter 

# parameters : used when we defined the function
# positional parameter : position matters
def hello(name, age):
    print(f'helloooo {name} {age}')
    
# Arguments : used when we called the function
# positional arguments
hello('Rutuja', '21')     # call/ Invoke the function 

#o/p: helloooo Rutuja 21

#---------------------------------------------------------------------------

# Defalut Parameter and Keyword Arguments 
 
# keyword arguments:
hello(age='20', name='Prerna')

# Defalut Parameters: 
def hello(name='Anuja Gholap', age='17'):
    print(f'helloooo {name} {age}')

hello()     # if forgot to give parameters then it takes defalut parameters

#o/p: helloooo Anuja Gholap 17


#--------------------------------------------------------------------------------

#return : 
    
def sum(num1, num2):
    num1+num2
print(sum(4,5))

# None 

#===============================

def sum(num1, num2):
    return num1+num2
# a function should do one thing really well.
# a function should return something.
print(sum(4,5))

#o/p: 9

#===================================================

def sum(num1, num2):
    def func(n1,n2):
        return n1+n2
    return func(num1, num2)
    return 5    # never going to print because above 'return' keyword exits a function  
    print('hello') # not going to print
total = sum(10,20)
print(total)

#o/p: 30

#---------------------------------------------------------------------------------------

# Methods and Functions: allows us to take actions on the data types
'''
#Functions: 
    
# Built in Functions in python:
list()
print()
max()
min()
input()

# custom functions :
def hello():
    pass

#-----------------------------

# Methods:
    
.method_name()   #syntax of name of the refernces

'''

'hello'.capitalize()
#o/p: Hello


#---------------------------------------------------------------------

# Docstrings: useful to add comments and definition to your function so that other people can understand 
    
def test(a):
    '''
    Info: this function tests and prints paramenter a 
    '''
    print(a)
print(test.__doc__)    # or help(test)

#o/p: Info: this function tests and prints paramenter a 

#--------------------------------------------------------------------------

# clean code:
    
def is_even(num):
    if num%2 == 0:
        return True
    elif num%2 !=0:
        return False
print(is_even(51))
#o/p: False
print(is_even(50))
#o/p: True

#==============================

# lets cleanup our code 

def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
print(is_even(51))
#o/p: False
print(is_even(50))
#o/p: True

#==============================

# Lets clean code more...

def is_even(num):
    if num%2 == 0:
        return True
    return False
print(is_even(51))
#o/p: False
print(is_even(50))
#o/p: True


# In more clear mannner:

def is_even(num):
    return num%2 == 0
   
print(is_even(51))
#o/p: False
print(is_even(50))
#o/p: True


#--------------------------------------------------------------------------


# *args : allows to grab positional argument and just sum everything 
# **kwargs:  allows us to grab any number of keyword arguments and get a dictionary 

# Rule of the ordering the parameters : 
# (parameters, *args, defalut parameters, **kwargs)
def argument_funct(*args):
    print(args)
    return sum(args)

print(argument_funct(1,2,3,4,5))

#o/p: 15  # sum will be printed


def argument_funct(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items 
    return sum(args) + total 

print(argument_funct(1,2,3,4,5, num1=5, num2=10))
#o/p: 30


#------------------------------------------------------------------------------

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
        return max(evens)
    
print(highest_even([10,2,3,4,8,11]))

# 10 


#------------------------------------------------------------------------

# Walrus Operator:(:=)  assigns values to variables as a part of a larger expression.
a = 'helloooooo'
if ((n := len(a)) > 10):   # n have the value of a 
    print(f'too long {n} elements')
    
while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]
    
#-------------------------------------------------------------------------------

# Scope: what variables do I have access to?

total = 100  # global scope because anybody can access it 

# function scope: 
if True:
    x = 10
def some_fuc():
    total = 100   # only have access within the function 
    print(total)
    
#-------------------------------------------------------------------------------

# Scope Rule: 

a = 1
def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(parent())     
print(a)

#o/p: 10
#     1 


# 1. start with local
# 2. Parent local 
# 3. Global
# 4. Built in python functions

#==========================================

a = 1
def parent():
    def confusion():
        return sum
    return confusion()

print(parent())     
print(a)

#o/p: <function sum at 0x000001B438E2FEB0>


#--------------------------------------------------------------------------


# Global Keyword:

a = 10 
def confusion(b):
    print(b)
    a = 90
confusion(300)
# o/p: 300   # prints 300 because b parameter is the part of the local scope


#===============================================

total = 0 
def count():
    global total 
    total += 1 
    return total 
count()
count()  
print(count())

# o/p: 3
'''
# if we defined total in the definition of the scope then even if we run the 
program many times it gives output as 1 only, because it checks function everytime

# for solving above problem we have to defined it as global for that use global keyword
global is the way for us to access a global varible

# but this this is not good way of doing things. 
'''

#================================================================

# better way is :
    
total = 0 
def count(total):
    total += 1 
    return total 
count()
count()  
print(count(count(count(total))))

#o/p: 3

#-----------------------------------------------------------------------------------------

# nonlocal keyword

def outer():
    x = 'local'
    def inner():
        nonlocal x    # if we comment this then o/p is outer : local
        x = 'nonlocal'  # assigning new stringand replacing 'local'
        print("inner:", x)
        
    inner()
    print("outer:", x)    # we have modified outer scope with the 'nonlocal'
outer()

'''
#o/p: 
    inner: nonlocal
    outer: nonlocal
    
    # here we have modified the  
'''

#------------------------------------------------------------------------------

# Why do we need scope? 

'''
Machine have limited power and memory.
In above code x have two location in memory.
python interpreter : clear the memory once job of function is over,
so garbage collector throws that function out form the memory.
'''

#------------------------------------------------------------------------------

# Python Developer tools:
# Terminal/ command promts
# Code Editor: Sublime Text, VS code (gives features like autocorrect, etc.)
# IDE's : PyCharm, Spyder, Jupyter (bigger and have lot of functions like debugging, code formatting, auto-testing, etc. )


#-------------------------------------------------------------------------------------------------------


