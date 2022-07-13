#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[5]:


def showDivisible(in_num):
    for ele in range(0,in_num):
        if(ele%5 == 0) and (ele%7 ==0):
            yield ele
for ele in showDivisible(100):
    print(ele,end=' ')


# Ans2)

# In[11]:


def genEvenNumbers(in_num):
    for ele in range(in_num+1):
        if ele%2 == 0:
            yield ele

for ele in genEvenNumbers(10):
    print(ele,end=' ')


# Ans3)

# In[13]:


def genFibonacci(in_num):
    if in_num == 0:
        return 0
    elif in_num ==1:
        return 1
    else:
        return genFibonacci(in_num-1)+genFibonacci(in_num-2)
print([genFibonacci(x) for x in range(20)])


# Ans4)

# In[14]:


def getUsernames():
    in_string = input('Enter emaol address(es): ')
    out_string = in_string.split('@')
    print(f'Username of {in_string} is {out_string[0]}')
    
for i in range(3):
    getUsernames()
    


# Ans5)

# In[16]:


class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length*self.length
    
square = Square(50)
print(square.area())

