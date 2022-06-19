#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[1]:


def factorial(num):
    if (num<1):
        return 1
    else:
        return num*factorial(num -1)
num = int(input('Enter a number:'))
value = factorial(num)
print(f'The factorial of {num} is {value}')


# Ans2)

# In[7]:


def generateTable(base,entries):
    for x in range(1,entries+1):
      print(f'{base} X {x} = {base*x}')
        
num = int(input('Enter a number: '))
values = int(input('Enter no if enteries:'))
generateTable(num,values)


# Ans3)

# In[2]:


s_count = int(input('Enter the no of fibonacci sequences you want?'))
initial_list = [0,1]
if s_count < 0:
    print('Fibonacci Numbers are not available for Negative Numbers')
elif s_count <= 2 and s_count >= 0:
    print(initial_list)
else:
    for ins in range(s_count):
        if ins >= 2 :
            initial_list.append(initial_list[ins-1]+initial_list[ins-2])
    print(f'The First{s_count} fibonacci series are : ', initial_list)


# Ans4)

# In[5]:


def checkArmstrongNumber():
    in_num = input('enter a number:')
    sum = 0
    for char in range(len(in_num)):
        sum = sum + pow(int(in_num[char]),3)
    if sum == int(in_num):
        print(f'{in_num} is a ArmStrong Number ')
    else :
        print(f' {in_num} is not a Armstrong Number ')
for x  in range(2):
    checkArmstrongNumber()
        


# Ans5)

# In[6]:


def checkArmstrongNumber(in_num, storage):
    sum = 0
    for char in range(len(in_num)):
        sum = sum + pow(int(in_num[char]),3)
    if sum == int(in_num):
        storage.append(int(in_num))

start_interval = int(input('Enter the Start of the Interval: '))
end_interval = int(input('Enter the End of the Interval: '))
list_of_armstrong = []

if start_interval > end_interval:
    print("Start Interval Cannot be Greater than End Interval")
else:
    for number in range(start_interval,end_interval+1):
        checkArmstrongNumber(str(number),list_of_armstrong)
    print(f'The Armstrong numbers between {start_interval} and {end_interval} are {list_of_armstrong}')


# Ans6)

# In[8]:


def SumofNaturalNumbers(num):
    sum = num*((num+1)/2)
    print(f'Sum of {num} natural number is {sum}')

num = int(input('enter a number: '))
SumofNaturalNumbers(num)


# In[ ]:




