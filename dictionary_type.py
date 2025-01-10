# dictionary : data type in python but it also a data structure.
# is used to organize the data
# curly brackets denotes a dictionary, dictionary is an unordered key-value pair,
# a key is a string for us to grab a value. 
dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x':True
}
print(dictionary['a'][1])
#o/p:2

my_list = [
    {
        'a': [1,2,3],
        'b': 'hello',
        'x':True
    },
    {
        'a': [4,5,6],
        'b': 'hello',
        'x':True
    }
]
print(my_list)
#[{'a': [1, 2, 3], 'b': 'hello', 'x': True}, {'a': [4, 5, 6], 'b': 'hello', 'x': True}]
print(my_list[0]['a'][2])
#o/p:3

#-------------------------------------------------------------------

# a dictionary dones not sorted, a list has order, it has indexes
# a dictionary has no order.
# dictionary stores more information than list because list has single value, list has the index and whatever the value is

#--------------------------------------------------------------------

# Dictionary keys:
    # key needs to be immutable, key is value that cannot change
    # list can be change, so key should not a list 
    # we can use tuple as a key
    # a key in a dictionary has to be unique because there can only be one key
    # key has to be unique.
dictionary = {
    '123': [1,2,3],
    True: 'hello',
    [100]:True
}
print(dictionary)
#o/p:TypeError: unhashable type: 'list'  # this is because of [100]

dictionary = {
    '123': [1,2,3],
    True: 'hello',
    100: True
}
print(dictionary)
#o/p: {'123': [1, 2, 3], True: 'hello', 100: True}

#--------------------------------------------------------------------

#dictionary methods:
    
user = {
        'basket' : [1,2,3],
        'greet' : 'hello'
}

print(user.get('age'))  # '.get' is a method on the object or the dictonary in python.
#o/p: None

#===========================================
user = {
        'basket' : [1,2,3],
        'greet' : 'hello'
}

print(user.get('age',55)) 
#o/p: 55  ....if value for age key does not exists then use 55 as default value.
#============================================

user = {
        'basket' : [1,2,3],
        'greet' : 'hello'
}
user2 = dict(name='rutuja')
print(user2)
#o/p:{'name': 'rutuja'}

#--------------------------------------------------------------------------

user = {
        'basket' : [1,2,3],
        'greet' : 'hello',
        'age':20
}
print('basket' in user)
#o/p:True
print('size' in user)
#o/p:False

# there are many dictionary methods in python 

#keys method:
print('age' in user.keys())
#o/p: True
print('hello' in user.values())
#o/p: True

#item:
print(user.items())
#o/p: dict_items([('basket', [1, 2, 3]), ('greet', 'hello'), ('age', 20)])

#clear:
print(user.clear())
#o/p:None

user.clear()   # creates an empty dictionary
print(user)
#o/p: {}   ...empty object/dictionary

#copy: allows a copy a user
user = {
        'basket' : [1,2,3],
        'greet' : 'hello',
        'age':20
}
user2 = user.copy()
print(user)
print(user2)
# o/p: 
# '''
#     {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
#     {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
#     '''
#=================================
user = {
        'basket' : [1,2,3],
        'greet' : 'hello',
        'age':20
}
user2 = user.copy()
print(user.clear())
print(user2)
#o/p: 
#    None
#   {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}

#pop: pop returns the value of whatever got removed.
user = {
        'basket' : [1,2,3],
        'greet' : 'hello',
        'age':20
}
print(user.pop('age'))
#o/p: 20
print(user)
#o/p: {'basket': [1, 2, 3], 'greet': 'hello'}  ...age is removed
#======================================
user = {
        'basket' : [1,2,3],
        'greet' : 'hello',
        'age':20
}
print(user.popitem())  #...it randomly pops up something one of the key and the value
print(user)
#o/p:
    # '''
    # ('age', 20)
    # {'basket': [1, 2, 3], 'greet': 'hello'}
    # '''

#update:
user = {
        'basket' : [1,2,3],
        'greet' : 'hello',
        'age':20
}
print(user.update({'age':55}))
print(user)
#o/p: {'basket': [1, 2, 3], 'greet': 'hello', 'age': 55}  ...age got updated
