#!/usr/bin/env python
# coding: utf-8

# Ans1) There are two boolean data types they are True and False.True and False first letter will be in uppercase and other word will be in lowercase.

# In[1]:


p = True
k = False
print(p,type(p))
print(k,type(k))


# Ans2)There are three types of boolean operator in python.They are as follows-:
#  a)are
#  b)and
#  c)not.

# Ans3)Truth table of boolean tables are as follows:-
#  a) Truth table for And Operator
#     True and True is True
#     True and False is Flase
#     False and True is False
#     False and False is False
#     
#  b) Truth table for Or operator
#     True and True is True
#     True and False is True
#     False and True is True
#     False and False is False
#     
#  c) Truth table for Not operator
#      True Not is Flase 
#      False not in True.
#      

# Ans4) 

# In[7]:


print((5>4) and (3==5)) # Flase
print(not(5>4)) # Flase
print((5>4)or(3==5)) # False
print(not((5>4)or(3==5))) # False
print((True and True)and(True==False)) # False
print((not False)or(not True))  # True


# Ans5) The Six Comparision operators are follows in python are-:
# ==, !=, <, >, <=, =>

# Ans6) The == is equal to operator that compares two values and evalutes to a Boolean, while = is that assignment operator that stores a value in a variable. 

# In[9]:


a=7
if a==7  :
    print(a==7)


# Ans7)

# In[12]:


spam = 0
if spam == 10:
    print('eggs') #bl0ck1
if spam > 5:
    print('bacon') #block2
else:
    print('ham')   #block3
print('spam')
print('spam')


# Ans8)

# In[15]:


def spamCode(spam) :
  if spam == 1:
      print('Hello')
  elif spam == 2:
    print('Howdy')
  else:
    print('Greetings!')
    
spamCode(1)
spamCode(2)
spamCode(3)


# Ans9) When program is stuck in endless lop then we have ot press Ctrl+c.

# Ans10) Break is a reserved keyword which is used to break the loop if break conditin is satisfied.
# Where as Continue will continue triggered towards loop.Code control will be go to continue.

# Ans11) The range difference between range(10),range(0,10) and range(0,10,1) are as follows-:
# a)Range(10) calls range from 0 to 9 but will not include 10 because of 10 is exclude.
# b)Range(0,10) will tell to start the loop from 0
# c)Range(0,10,1) will tell the loop to increase the variable by 1 on each iteration.

# Ans12)

# In[23]:


for i in range(1, 11):
    print(i)


# In[22]:


i = 1 
while i <= 10: 
    print(i) 
    i += 1 


# Ans13) The function can be called with spam.bacon()

# In[ ]:





# In[ ]:





# In[ ]:




