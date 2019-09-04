# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:48:12 2019

@author: BSDU
"""

"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse2.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a integer.
    Take input from User  
  Input: 
    -321
  Output:
    -123  
"""
user1 = input("Enter the number").strip()

#"-"+user1[1:][::-1]

def reverse(user1):
    if len(user1)==0:
        return(user1)
        
    else:
        y = user1[1:]+user1[0]
        
        return y[::-1]

x = reverse(user1)
print(x)
