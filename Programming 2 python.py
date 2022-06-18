#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[10]:


def kmToMiles():
    kiloMeters = float(input("Enter no of kilometers"))
    print("{} km is equal to {} miles".format(kiloMeters,kiloMeters*0.621))
    
kmToMiles()


# Ans2)

# In[20]:


def celToFarh():
    celsius = int(input("enter temperature in celsius :"))
    Farenheit = (celsius*(9/5))+32
    print("{} celsius is equal to {}  Farenheit".format(celsius,Farenheit))
    
    
celToFarh()


# Ans3)

# In[32]:


# import module
import calendar
def showCalender():
    year = int(input("Enter calender year: "))
    print(calendar.calendar(year))
    
showCalender()


# Ans5)

# In[33]:


num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))


def swapNumbers(num_1,num_2):
        print('Before Swapping',num_1,num_2)
        num_1 = num_1+num_2
        num_2 = num_1-num_2
        num_1 = num_1-num_2
        print('before Swapping',num_1,num_2)

swapNumbers(num_1,num_2)

