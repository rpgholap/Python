# Conditional Logic:
    
is_old = True
is_licenced = True
'''
if condition:
    body of if condition
    (runs until if condition is true)
elif another_condition:
    body of elid
    (runs when if condition is false/ not satisfied and another_condition is true)
else:
    body of else 
    (runs when if condition is false)
'''

if is_old:
    print('you are old enough to drive!')
elif is_licenced:
    print('you can drive now!')
else:
    print('you are not of age!')
    
print('okok')

# but problem occur when person is old enough to drive and have a licence also 
if is_old and is_licenced:   #if both condition are true then only true otherwise false
    print('you are old enough to drive and you have a licence!')
else:
    print('you are not of age!')
    
print('okok')




#------------------------------------------------------------------------------
#indentation in python: 4 is standaed space for indentation

#------------------------------------------------------------------------------

# Truthy vs Falsey:

is_old = bool('hello')
is_licenced = bool(5)  
print(bool('hello'))
print(bool(5))
'''
o/p:
    True
    True
'''
print(bool(''))
print(bool(0))
'''
#o/p: 
    False
    False
'''

#------------------------------------------------------------------------------

# ternary operator: also called as conditional expressions 

# condition_if_true if condition else condition_if_false

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)
# o/p: message allowed 
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)
# o/p: not allowed to message 

#------------------------------------------------------------------------------

# #short circuiting: 
is_friend = True
is_user = True
print(is_friend and is_user)
# o/p: True

if is_friend or is_user:     # or says if either one of these conditions are true then run that block of code
    print('BFF')

#---------------------------------------------------------------------------------

# logical operators : and , or, < >, == , <= , >= , != , not

print(4>5)
#op:False
print(4<5)
#op: True
print(4==5)
#op: False

print('a'>'b') #why a grater than b .....Google it.....
#o/p: False
print('a'>'A')
#o/p: True
print(1>=0)
#o/p: True
print(1<=0)
#o/p: False
print(0!=1)
#o/p: True

print(not(True))
#o/p: False
print(not(False))
#o/p: True
print(not(1==1))
#o/p: False

#------------------------------------------------------------------------------

# Exercise: Logical operator
is_magician = False
is_expert = True

# check if magician AND expert: "You are a master magician"
if is_expert and is_magician:
    print("You are a master magician")
    
# check if magician but not expert: "At least you're getting there"
elif is_magician and not is_expert:  #
    print("At least you're getting there")
# check if you're not a magician: "You need magic powers"
elif not is_magician:
    print("You need magic powers")

#o/p: You need magic powers