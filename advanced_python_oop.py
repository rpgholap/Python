# What is OOP(Object Oriented Programming) ?
# Every thing in python is an object because in python everyting is build by the class keyword and 
# we are able to use different methods on objects to perform actions on them.
# Objects : Have methods and attributes that you can access using .(dot) method().
# We are breaking task into small pieces into 'little objects' that represents real world.
# OOP enables us to easy maintainence, extend and write, structure & organize a code. 
#


# OOP: 
'''
Objects have methods and attributes that we can access with the dot(.) method

OOP is the way to think about the code, to structure the code and easier to maintain, extend and write.
allows us to create objects that have their own methods and attributes.
'''

# build class
# Gaming compamy

#class is a blueprint  
class PlayerCharacter:
    def __init__(self, name, age):    # __init__ method: constructor 
        self.name = name       #attributes
        self.age = age 

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Rutuja', 21)
print(player1.name)
print(player1.age)

player2 = PlayerCharacter('Anuja', 17)
print(player2.name)
print(player2.age)

print(player1)
print(player2)
# both players are located in different places in memeory


# Attributes and Methods

class PlayerCharacter:
    membership = True     # it is class attribute, it will going to be true for all objects
                          # it does not change across instances 
    def __init__(self, name, age):    # __init__ method: constructor 
        self.name = name       #attributes
        self.age = age 

    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Rutuja', 21)
print(player1.name)
print(player1.age)

print(player1.membership)
#o/p: True

#------------------------------------------------------------------

class PlayerCharacter: 
    membership = True
    def __init__(self, name, age):    # __init__ method: constructor
        if(self.membership):          # class object attribute
        #if(PlayerCharacter.membership):    # also works here
            self.name = name       #attributes
            self.age = age 

    def shout(self):
        print(f'My name is{self.name}')

player1 = PlayerCharacter('Rutuja', 21)
print(player1.name)
print(player1.age)

print(player1.name)
print(player1.membership)
# Rutuja
# True



#------------------------------------------------------------------------

# __init__ : constructor function, called every time when we instentiate an object
