
# Strings: A piece of text or an orderd sequence of characters
type('hi hello there')
#o/p : str
username = 'supercoder'
long_string = '''
Wow
That's great
'''
print(long_string)   

first_name = 'Anuja'
second_name = 'Rutuja'
sisters = first_name + ' & ' + second_name
print(sisters)

#string concatenation
print('Hello' + ' World')
#o/p :'Hello World'
print('Hello' + 5)
#o/p :TypeError: can only concatenate str (not "int") to str

#------------------------------------------------------------------------------

#Type Conversion:
str(100)
type(str(100))
#o/p :str
#o/p :'100'

print(type(int(str(100))))   
'''
its like 
a = str(100)
b = int(a)
c = type(b)
print(c)
'''
#o/p: <class 'int'>

#------------------------------------------------------------------------------

# Escape Sequence:
weather = "It's sunny"
print(weather)
# weather = "It's "kind of" sunny"  # error
# for solving this error we use Escape Sequence
weather = "\t It\'s \"kind of\" sunny \n hope you have a nice day" 
# \t added a tab spacing to string 
# \n add a new line 
# slash(\) interpret wahtever comes after \ is considerd as string
print(weather)

#------------------------------------------------------------------------------

#formatted String
name = 'Rutuja'
age = 20
print('hi ' + name + '. You are ' + str(age) + ' Years old')
#o/p : hi Rutuja. You are 20 Years old
'''
add f at the beginning and this f at the beginning is going to tell python 
that the string is going to be a formatted string
Insted of doing + and name and all this stuff and doing str  to covert the type
we can simply add this 'f'
'''
print(f'hi {name}. You are {age} Years old')   #.....Better wayy....
#o/p : hi Rutuja. You are 20 Years old
print('hi {}. You are {} Years old'.format('Rutuja','20'))   # another way 
#o/p : hi Rutuja. You are 20 Years old
print('hi {}. You are {} Years old'.format(name,age))   # we can use variables also

print('hi {1}. You are {0} Years old'.format('Rutuja','20'))    
#o/p :hi 20. You are Rutuja Years old  ......in computer science we start counting from zero

print('hi {0}. You are {1} Years old'.format('Rutuja','20'))    

#--------------------------------------------------------------------------------

#String Indexes:
'''
One of the most important thing about the string is to access different part 
of a string using index

string Slicing : [start:stop:stopover]
'''
selfish = 'me me me'
selfish[0]
#o/p :'m'
selfish[7]
#o/p : 'e'

#[start:stop]
selfish[0:7]
# o/p : 'me me m'
selfish[0:8]
# o/p : 'me me me'

#[start:stop:stopover]
numbers = '012345678'
numbers[1:8:2]
#o/p :'1357'
numbers[1:]   #go to the end 
#o/p :'12345678'
numbers[:5]  #starts as default zero and goes to five
#o/p :'01234'
numbers[::1]  # start and end is notmention so all the string will be printed.
#o/p :'012345678'
numbers[-1]  # in python negative index means starts from end of the string
#o/p :'8' 
numbers[::-1]  # ********we get the reverse string***********
#o/p :'876543210'

#------------------------------------------------------------------------------

#immutability :
'''
Strings in Python are immutable that means they cannot be changed.
'''

numbers = '01234567'
numbers[0] ='8'
#o/p :TypeError: 'str' object does not support item assignment
# we cannot reassign a part of a string
# for changing the value we have to completely reassign the value or create new
numbers = '8'
print(numbers)

#------------------------------------------------------------------------------

# Built-in Functions + Methods
# we learned few built in functions like, str(), int(), float(), type(), print(), etc..

greet = 'helooooo'
len('helooooo')
#o/p : 8
print(greet[0:len(greet)])
#o/p :helooooo

# Methods : Ex. .format()

quote = 'to be or not to be'
quote.upper()
#o/p: 'TO BE OR NOT TO BE'
print(quote.capitalize())
print(quote.find('be'))
#o/p : 3
print(quote.replace('be','me'))
#o/p:to me or not to me
print(quote)
#o/p: to be or not to be   # not changed because strings are immutable

#------------------------------------------------------------------------------

#Booleans : True or False

name = 'Rutuja'
is_cool = False
is_cool = True
print(bool('True'))

bool(1)
#o/p:True
bool(0)
#o/p:False

#------------------------------------------------------------------------------

# Exersise: Type Conversion
birth_year = input('What year where you born?')
age = 2023 - int(birth_year)  # we have to convert birth_year into int 
print(f'your age is:{age}')
#o/p:your age is:20

#------------------------------------------------------------------------------

# commenting the code :
'''
'#' tells the python interpreter that this is a comment dont run it .
comment is only for understanding the code more efficiently.
add comments in a code when something in the code is really really important 
'''

#------------------------------------------------------------------------------

# Exersise for password checker:
username = input('What is your username?')
password = input('\n What is your password?')
password_length = len(password)
hidden_password = '*' * password_length
print(f'{username}, your password, {hidden_password}, is {len(password)} letters long')
#o/p:Rutuja, your password, **********, is 10 letters long
