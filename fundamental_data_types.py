# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:23:31 2023

@author: rutuja

Complete Python Developer : Zero to Mastery

"""

#__________________Numbers_____________________

#Fundamental Data Types:
    
# 1.Int (A number)
# 2.float (A number with a decimal)

print(2+4)
print(2-4)
print(2*4)
print(2/4)  #Floting point number
print(type(2/4))
print(type(2+4))
print(2 ** 3) #power
print(2 // 4) #return integer
print(5 % 4)  #gives a remainder
#Float number actually takes a lot more space in memory than an integer.

#Math Functions
print(round(3.9)) #Round off the number
print(abs(-20))   # abs tern the negative number into positive value

#operator precedance:
print(20-3*4)
# order: (), **, * /, + - 

#complex Number data type (real,imag)

print(bin(5))  #we get binary reprentation
#o/p : '0b101'
print(int('0b101',2))  #covert into a number that have base two
#o/p : 5