#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[1]:


def genFibonacci(n,a,b):
    if n == 0:
        return 1
    else:
        result = a+b
        print(result, end=' , ')
        genFibonacci(n-1,b,result)
in_num = int(input('enter the length of series: '))
print('0, 1', end=',')
genFibonacci(in_num,1,2)


# Ans2)

# In[3]:


def Factorial(num):
    if (num < 1):
        return 1
    else:
        return num*Factorial(num-1)
num = int(input('enter a number: '))
value = Factorial(num)
print(f'The Factorial of {num} is {value}')


# Ans3)

# In[5]:


def calculateBMI():
    in_weight = eval(input('Enter your Weight(kgs): '))
    in_height = eval(input('Enter your Height(mts): '))
    calc_bmi = in_weight/pow(in_height,2)
    if (calc_bmi < 18.5):
        status = 'Underweight'
    elif (calc_bmi >= 18.5 and calc_bmi < 24.9):
        status = 'Healthy'
    elif (calc_bmi >= 24.9 and calc_bmi < 30):
        status = 'Overweight'
    elif (calc_bmi >=30):
        status = 'Suffering from Obesity'
    print(f'Your\'re BMI is {calc_bmi} and status is {status} ')
calculateBMI()


# Ans4)

# In[11]:


import math
def genNatLog():
    in_num = eval(input("Enter a Number:"))
    print(math.log(in_num))

genNatLog()


# Ans5)

# In[12]:


def cubeOfNaturalNumbers():
    in_num = int(input("Enter the no of Natural Numbers: "))
    result = pow(((in_num * (in_num +1))/2),2)
    print(f'The Cube Sum of First {in_num} Natural Numbers is {result}')

cubeOfNaturalNumbers()

