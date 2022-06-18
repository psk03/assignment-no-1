#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[1]:


print("hello Python")


# Ans2)

# In[2]:


val1 = 10
val2 = 20

sum = val1 + val2  #addition
print(sum)


# In[3]:


val1 = 50
val2 = 2

div = val1/val2
print(div)


# Ans3)

# In[10]:


# Python Program to find the area of triangle

a = 5   
b = 6
c = 7

s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5   # calculate the area
print('The area of the triangle is %0.2f' %area)


# Ans4)

# In[11]:


dev_1 = int(input("enter first number"))
dev_2 = int(input("enter second number"))

def swapnumbers(a,b):
    temp = a
    a = b
    b = temp
    return a,b
print('Before swapping ->', dev_1, dev_2)
dev_1, dev_2 = swapnumbers(dev_1 , dev_2)

print('After swapping ->' , dev_1, dev_2)


# Ans5)

# In[13]:


from random import randint 

def generateRandomNumber(start = 0, end = 20000):
    print('Random number ->', randint(start,end))
    
generateRandomNumber()   # without argument


generateRandomNumber(0,150)  # with argument


# In[ ]:




