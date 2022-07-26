#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[2]:


def evenDivisible(a,b,c):
    divlist = []
    for num in range(a,b+1):
        if num%c == 0:
            divlist.append(num)
    print(f'{a,b,c} {sum(divlist)}')
    
evenDivisible(1,10,20)
evenDivisible(1,10,2)
evenDivisible(1,10,3)


# Ans2)

# In[3]:


def checkEquality():
    in_string = input('Enter the inequality:')
    out_bool = eval(in_string)
    print(f'{in_string} {out_bool}')
    
for x in range(3):
    checkEquality()


# Ans3)

# In[4]:


def replaceVowels():
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    in_string = input("String: ")
    in_string_copy = in_string
    in_char = input('Replacement character: ')
    for ele in in_string:
        if ele in vowels:
            in_string = in_string.replace(ele,in_char)
    print(f'{in_string_copy} {in_char} ➞ {in_string}')
            
for x in range(3):
    replaceVowels()


# Ans4)

# In[5]:


def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)


print(f'factorial(5) ➞ {factorial(5)}')
print(f'factorial(3) ➞ {factorial(3)}')
print(f'factorial(1) ➞ {factorial(1)}')
print(f'factorial(0) ➞ {factorial(0)}')


# Ans5)

# In[6]:


def genHamDistance():
    in_string_1 = input('Enter the String_1: ')
    in_string_2 = input('Enter the String_2: ')
    if len(in_string_1) == len(in_string_2):
        count = 0
        for i in range(len(in_string_1)):
            if in_string_1[i] != in_string_2[i]:
                count = count+1
        print(f'Hamning Distance b/w {in_string_1} and {in_string_2} ➞ {count}')
    else:
        print('Both Strings Must be of Same Length')

for x in range(3):
    genHamDistance()

