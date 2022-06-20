#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[3]:


def findtheLcm(x_term,y_term):
    if x_term > y_term:
        greater = x_term
    else:
        greater = x_term
    while True:
        if((greater%x_term == 0) and (greater%y_term == 0)):
            lcm = greater
            break
        else:
            greater +=1
    print(f'The LCM of {x_term}, {y_term} is {lcm}')
findtheLcm(4,8)
findtheLcm(2,6)
findtheLcm(5,100)


# Ans2)

# In[6]:


def findTheHcf(x_term,y_term):
    if x_term>y_term:
        smaller = y_term
    else:
        smaller = x_term
    for ele in range(1,smaller+1):
        if((x_term%ele == 0) and (y_term%ele == 0)):
            hcf = ele
    print(f'The HCF of {x_term},{y_term} is {hcf}')

findTheHcf(33,89)
findTheHcf(2,3)
findTheHcf(10,23)


# Ans3)

# In[7]:


def DecimalToOther():
    num = int(input("enter a number:"))
    print(f'Binary number -> {bin(num)}')
    print(f'Octal number -> {oct(num)}')
    print(f'Hexadecimal number -> {hex(num)}')
    
DecimalToOther()
    
    
    


# Ans4)

# In[8]:


def charToAscii():
    char = input('Enter a Character: ')
    if len(char) > 1:
        print('Plese enter a Single Character')
    else:
        print(f'Ascii Character of {char} is {ord(char)}')
charToAscii()


# Ans5)

# In[1]:


import operator

ops = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv } 

print('Select a Arithmetic Operation:         \n1.Addition(+)        \n2.Substraction(-)        \n2.Multiplication(*)        \n4.Division(/)        \n3.Stop(0)\n')
   

while True:
    operator = input('Enter a arithmetic operation -> ')
    if operator == '0':
        print("Program Stopped successfully")
        break
    elif operator not in ['+','-','*','/']:
        print("Please enter a valid operator")
    else:
        num_1 = int(input('\nEnter 1st Number: '))
        num_2 = int(input('Enter 2nd Number: '))
        print(f'{num_1}{operator}{num_2}={ops[operator](num_1,num_2)}\n')


# In[ ]:





# In[ ]:




