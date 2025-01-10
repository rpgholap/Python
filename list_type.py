
# list datatype : an ordered sequence of objects that can be of any type.
# we denote list in [] 'square brackets'
# in python list in the form of array.
# list are mutable.
a,b,c = 1,2,3
l1 = [1,2,3,4,5]
l2 = [1,2,a,True]

# data structure : to organize information and data 

amezon_cart = ['notebooks', 'sunglasses']
print(amezon_cart[0])
#o/p:notebooks

#list Slicing :
amezon_cart = [
    'notebook',
    'sunglasses',
    'toys',
    'grapes'
    ]
'''
greet = 'hello'
greet[0]='z'
#o/p:TypeError: 'str' object does not support item assignment
'''
print(amezon_cart[0:2])
#o/p:['notebook', 'sunglasses']

# copying and modify like concept:
amezon_cart[0] = 'laptop'   #lists are mutable   
#o/p:['laptop', 'sunglasses', 'toys', 'grapes']
new_cart = amezon_cart[:]    # colon indicates that we wan't to create a copy of the list
new_cart[0] = 'gum'
print(new_cart)
print(amezon_cart)
'''
#o/p:['gum', 'sunglasses', 'toys', 'grapes']  # new cart get change as per requirements
['laptop', 'sunglasses', 'toys', 'grapes']
'''

#Matrix: a matrix is a way to describe 2D lists or multi-dimentional lists
matrix = [
          [1,2,3],
          [2,4,6],
          [7,8,9]
         ]

print(matrix[0][1])
#o/p:2

#List Methods:
    
basket = [1,2,3,4,5]
len(basket)
#o/p:5

#adding:
new_list = basket.append(100)
print(basket)
#o/p:[1, 2, 3, 4, 5, 100]
print(new_list)
#o/p: None
#=================================
#adding
basket.append(100)
new_list = basket
print(basket)
#o/p:[1, 2, 3, 4, 5, 100]
print(new_list)
#o/p:[1, 2, 3, 4, 5, 100]
#================================
basket.insert(4, 50)
new_list = basket
print(basket)
#o/p:[1, 2, 3, 4, 50 , 5]
print(new_list)
#o/p:[1, 2, 3, 4, 50, 5]
#================================
basket.extend([51])
new_list = basket
print(basket)
#o/p:[1, 2, 3, 4, 50 , 5, 51]
print(new_list)
#o/p:[1, 2, 3, 4, 50, 5, 51]
#=================================

#removing 
basket = [1,2,3,4,5]
basket.pop(0)  # it removes 0 index value .... pop just display what is going to remove
basket.remove(4)  # it removes value 4
basket.clear()  # empty list
print(basket)


basket = ['a','b','c','d','e','d']
print(basket.index('d', 0, 4))
#o/p:3
print('d' in basket)
#o/p:True
print('x' in basket)
#o/p:False

print(basket.count('d')) #counts how many times d occurs in the list
#o/p:2

print(basket.sort())   # sort : sorts the list / modifies the list
#o/p: None 

basket = ['a','b','x','c','d','e','d']
basket.sort()
print(basket)
#o/p:['a', 'b', 'c', 'd', 'd', 'e','x']

basket = ['a','b','x','c','d','e','d']
new_basket = basket.copy()
new_basket.sort()
print(new_basket)
print(basket)
'''
#o/p:
['a', 'b', 'c', 'd', 'd', 'e', 'x']
['a', 'b', 'x', 'c', 'd', 'e', 'd']
'''

basket = ['a','b','x','c','d','e','d']
basket.reverse()  # only reverse the list
print(basket)
#o/p:['d', 'e', 'd', 'c', 'x', 'b', 'a']

basket = ['a','b','x','c','d','e','d']
basket.sort()
basket.reverse()
print(basket)
#o/p:'x', 'e', 'd', 'd', 'c', 'b', 'a']   #sorted and reversed list

#-----------------------------------------------------------------------
basket = ['a','b','x','c','d','e','d']
basket.sort()
#o/p:['a', 'b', 'c', 'd', 'd', 'e', 'x']
basket.reverse()
#o/p:['x', 'e', 'd', 'd', 'c', 'b', 'a']
print(basket[::-1])
#o/p:['a', 'b', 'c', 'd', 'd', 'e', 'x']
print(basket)
#o/p:['a', 'b', 'c', 'd', 'd', 'e', 'x']
#    ['x', 'e', 'd', 'd', 'c', 'b', 'a']

#range
print(list(range(1,100)))  #range(start,stop)
print(list(range(101)))

sentence = '!'
sentence.join(['hi', 'my','name','is','rutuja'])
#o/p:'hi!my!name!is!rutuja'
sentence = ' '
sentence.join(['hi', 'my','name','is','rutuja'])
#o/p:'hi my name is rutuja'

#---------------------------------------------------------------------

#List unpacking
a,b,c = [1,2,3]
print(a)
print(b)
print(c)

a,b,c,*other = [1,2,3,4,5,6,7,8]
print(a)
print(b)
print(c)
print(other)
'''
#o/p: 
1
2
3
[4, 5, 6, 7, 8]
'''

#---------------------------------------------------------------------

# None : special data type in python used to repersent the absence of value.
# we also know the 'NULL' which is another way to reperesent the absence of value.
a = None
print(a)
#o/p: None

#---------------------------------------------------------------------