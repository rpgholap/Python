# set: unordered collections of unique objects

my_set = {1,2,3,4,5,5}   # we just created a set
print(my_set)
#o/p:{1, 2, 3, 4, 5} ....5 returns only one time because set gives unique values
my_set.add(100)
#o/p:{1, 2, 3, 4, 5, 100}
my_set.add(2)
#o/p:{1, 2, 3, 4, 5, 100} ...not going to add another 2 because 2 is already in a set
#===========================================

# task is to create or return a list or a collection that has only unique items

my_list = [1,2,3,4,5,5]
print(set(my_list))
#o/p:{1,2,3,4,5}   ...set removes duplicate values
# we can use in case of emails and passward in our projects

#==============================================================

#set object is not supports to indexes
my_set = {1,2,3,4,5,5}
print(my_set[0])   #gives error
print(1 in my_set)
#o/p: True
print(len(my_set))
#o/p:6

my_set = {1,2,3,4,5,5}
new_set = my_set.copy()
my_set.clear()
print(new_set)
#o/p:{1, 2, 3, 4, 5}
print(my_set)
#o/p:set()....because of clear

#------------------------------------------------------------------------------

my_set = {1,2,3,4,5}
your_set = (4,5,6,7,8,9,10)
print(my_set.difference(your_set))
print(my_set)
#o/p:{1, 2, 3}
#    {1, 2, 3, 4, 5}
print(my_set.discard(5))
#o/p:None
print(my_set)
#o/p:{1,2,3,4}  ....we discarded 5
print(my_set.difference_update(your_set))   #removes all elements of another set from this set
print(my_set)
#o/p:{1, 2, 3}
print(my_set.intersection(your_set))
#o/p:{4, 5}
print(my_set.isdisjoint(your_set))
#o/p:False # not disjoint sets 
print(my_set.union(your_set))
#o/p:{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  ...removes duplicates and takes union to sets

my_set = {4,5}
your_set = (4,5,6,7,8,9,10)
print(my_set.issubset(your_set))
#o/p: Ture
print(my_set.issuperset(your_set))
#o/p: False
