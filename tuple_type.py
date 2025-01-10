
# Tuple: are like lists, but unlike lists we cannot modify them
# they are immutable
my_tuple = (1,2,3,4,5)
my_tuple[1] = 'z'   #TypeError: 'tuple' object does not support item assignment
# a tuple is immutable once you created you cannot modify it.
print(my_tuple[1])
#o/p:2
print(5 in my_tuple)
#o/p:True

# If you don't need to change the list, that makes things easier because it tells other programmer looking at your code that this shouldn't be change.t
# tuple makes the things easier and more efficient
# tuple makes your code safer because people can modify it, makes code more predictable 
# but it is less flexible that a list that we can't sort data,can't run reverse on tuple 
# but other good thing is that they are slightly more performant than lists, they are usually faster than lists.
# if you don't need a list to change use a tuple.
  
#------------------------------------------------------------------------------

my_tuple =(1,2,3,4,5)
new_tuple = my_tuple[1:4]
print(new_tuple)
#o/p: (2,3,4)  ...returns a tuple

#================================
x,y,z,*other = (1,2,3,4,5)
print(x)
#o/p:1
print(z)
#o/p:3
print(other)
#o/p:[4,5]

#================================

my_tuple =(1,2,4,3,4,5,5)
print(my_tuple.count(5))
#o/p: 2   ...counts how many 5 are there in the tuple
print(my_tuple.index(5))
#o/p: 5
print(len(my_tuple))
#o/p: 7