#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[5]:


def sumOfArray():
    in_arr = eval(input("Enter the Array: "))
    print(f'The sum of {in_arr} is {sum(in_arr)}')

sumOfArray()


# Ans2)

# In[9]:


def largestElement():
    in_arr = eval(input("enter the array: "))
    print(f'The largest element in {in_arr} is {sorted(in_arr, reverse=True)[0]}')
    
largestElement()


# Ans3)

# In[10]:


def reverseofArray():
    in_arr = eval(input("enter the array: "))
    print(f"The reverse of array {in_arr} is {in_arr[::-1]}")
reverseofArray()


# Ans4)

# In[11]:


def sumOfSplits():
    in_arr = eval(input("Enter the Array: "))
    print(f"The Sum of First and Last Elements of Array {in_arr} is {in_arr[0]+in_arr[-1]}")
    
sumOfSplits()


# Ans5)

# In[13]:


def checkMonotonic():
    in_arr = eval(input("Enter the Array: "))
    if(all(in_arr[i]<=in_arr[i+1] for i in range(len(in_arr)-1)) or all(in_arr[i]>=in_arr[i+1] for i in range(len(in_arr)-1))):
        print(f'Array {in_arr} is Monotonic')
    else:
        print(f'Array {in_arr} is Not Monotonic')

checkMonotonic()
checkMonotonic()

