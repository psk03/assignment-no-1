#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[6]:


from math import sqrt
def calculateProgram():
    in_num = eval(input("Enter the Input: "))
    out_num = []
    C = 50 # Declaring and initializing constant C
    H = 30 # Declaring and initializing constant H
    for ele in in_num:
        Q = str(int(sqrt((2*C*ele)/H)))
        out_num.append(Q)
    print("Output: {}".format(','.join(out_num)))
    
calculateProgram()


# Ans2)

# In[10]:


import array as arr
def generateArray():
    in_x = int(input('Enter the no of rows:'))
    in_y = int(input('Enter tne no of Columns'))
    out_array = []
    for ele in range(in_x):
        out_array.insert(in_x,[])
        for sub_ele in range (in_y):
                out_array[ele].append(ele*sub_ele)
    print(out_array)
    
generateArray()
    


# Ans3)

# In[13]:


def sortString():
    in_string = input("Enter the Input String: ")
    out_string = ','.join(sorted(in_string.split(',')))
    print(f'Output: {out_string}')
    
sortString()


# Ans4)

# In[14]:


def sortAlphaNumerically():
    in_string = input("Enter the Input String: ")
    out_string = ' '.join(sorted(sorted(list(set(in_string.split(" "))))))
    print(f'Output: {out_string}')
    
sortAlphaNumerically()


# Ans5)

# In[15]:


def countLetterAndDigits():
    in_string = input("Enter the Input String: ")
    lettersList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    digitsList = '0123456789'
    letters = 0
    digits = 0
    for ele in in_string:
        if ele in lettersList:
            letters += 1
        if ele in digitsList:
            digits += 1
    print(f'LETTERS {letters} \nDIGITS {digits}')
        
countLetterAndDigits()


# Ans6)

# In[16]:


def checkPassword():
    in_string = input("Enter the Input String: ")
    small_list = "abcdefghijklmnopqrstuvwxyz"
    cap_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num_list = "0123456789"
    special_list = "$#@"
    for ele in in_string.split(","):
        if len(ele) <= 12 and len(ele) >=6 :
            if any(i.isupper() for i in ele):
                if any(i.islower() for i in ele):
                    if any(i for i in ele if i in special_list):
                        print(ele)
                               
checkPassword() 

