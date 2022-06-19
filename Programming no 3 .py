#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[3]:


def checkNumber(num):
    if num > 0:
        print("{} is a Positive number".format(num))
    elif num < 0 :
        print("{} is a Negative number".format(num))
    else:
        print("Number is Zero")
num = int(input("Enter a number:"))
checkNumber(num)


# Ans2)

# In[4]:


def checkNumber(num):
    if num%2 == 0:
        print("{} is a Even number".format(num))
    else:
        print("{} is a Odd number".format(num))
num  = int(input("Enter a number : "))
checkNumber(num)


# Ans3)

# In[5]:


def checkYear(year):
    if (year%4 == 0 and year%100 !=0 or year%400 == 0):
         print(f"{year} is  Leap year")
    else :
         print(f"{year} is not  Leap year")
            
year = int(input("Enter a year:"))
checkYear(year)
   
    


# Ans4)

# In[8]:


def isPrime(num):
    flag = False
    for i in range(2,num):
        if num%i == 0:
            flag = True
            break
    if(not flag):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
number = int(input("Enter a number :"))
isPrime(number)


# Ans5)

# In[9]:


primeNumbersList = []

def generatePrimeNumbers():
    for a in range (1,10000):
        flag = False
        for b in range (2,a) :
            if(a%b == 0):
                flag =True
                break
        if(not flag):
            primeNumbersList.append(a)
generatePrimeNumbers()
print(primeNumbersList)


# In[ ]:




