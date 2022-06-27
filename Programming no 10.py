#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[4]:


def sumofList():
    in_ele = int(input('Enter the no of enteries in a list: '))
    in_list = []
    for itr in range(in_ele):
        in_list.append(int(input('Enter a element: ')))
    print(f' Sum of Elements : {sum(in_list)}')
sumofList()    


# Ans2)

# In[5]:


def mulofList():
    in_ele = int(input('Enter the no of enteries in a list: '))
    in_list = []
    mul = 1
    for itr in range(in_ele):
        in_list.append(int(input('Enter a element:')))
    for ele in  in_list:
        mul = mul * ele
    print(mul)
    
mulofList()


# Ans3)

# In[3]:


def smalleleinList():
    in_ele = int(input('Enter the no of elements in a list:'))
    in_list = []
    for ele in range(in_ele):
        in_list.append(int(input('enter a element:')))
    print(f'The smallest element in {in_list} is {sorted(in_list)[0]}')
smalleleinList()


# Ans4)

# In[1]:


def largesteleinList():
    in_ele = int(input('Enter the no of elements in a list:'))
    in_list = []
    for ele in range(in_ele):
        in_list.append(int(input('enter a element:')))
    print(f'The Largest element in {in_list} is {sorted(in_list, reverse=True)[0]}')
largesteleinList()


# Ans5)

# In[3]:


def secondlargesteleList():
    in_ele = int(input('Enter the no of elements in a list:'))
    in_list = []
    for ele in range(in_ele):
        in_list.append(int(input('enter a element:')))
    print(f'The Second Largest element in {in_list} is {sorted(in_list, reverse=True)[0]}')
secondlargesteleList()


# Ans6)

# In[4]:


def nlargesteleinList(k):
    in_ele = int(input('Enter the no of elements in a list:'))
    in_list = []
    for ele in range(in_ele):
        in_list.append(int(input('enter a element:')))
    print(f'The {k} largest element in {in_list} is {sorted(in_list, reverse=True)[0:k]}')
nlargesteleinList(4)


# Ans7)

# In[5]:


def evennoinList():
    in_ele = int(input('Enter the no oe elements in a list:'))
    in_list = []
    even_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a element:')))
    for ele in in_list:
        if ele%2  == 0:
            even_list.append(ele)
    print(f'The even number in {in_list} are {even_list}')
    
evennoinList()


# Ans8)

# In[12]:


def oddnoinList():
    in_ele  = int(input('Enter the no of elements in a list: '))
    in_list = []
    odd_list = []
    for ele in range(in_ele):
        in_list.append(int(input('Enter a element:')))
    for ele in in_list:
        if ele%2 !=0:
            odd_list.append(ele)
    print(f'The even element in {in_list} are {odd_list}')
    
oddnoinList()


# Ans9)

# In[15]:


def checkEmptyList():
    in_list = eval(input('Enter all elements of the list: '))
    if [] in in_list:
        print(f'There is an Empty list in {in_list} at Position {in_list.index([])}')
        in_list.remove([])
        print(f'The List after removing [] is {in_list}')
    else:
        print(f'There is no [] List in the list {in_list}')
        
checkEmptyList()


# Ans10)

# In[20]:


import copy


def cloneList():
    in_list = eval(input('Enter a list'))
    print(in_list, id(in_list))
    cloned_list = in_list.copy()
    print(cloned_list, id(cloned_list))
    
cloneList()


# Ans11)

# In[24]:


def checkOccurence():
    in_list = eval(input('Enter the elements of the list: '))
    in_num = eval(input('Enter the element to find: '))
    count = 0
    if in_num in in_list:
        for ele in in_list:
            if ele == in_num:
                count = count+1
    print(f'There are {count} occurences of {in_num} in {in_list}')
    
checkOccurence()

