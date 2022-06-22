#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[1]:


print(60*60)


# Ans2)

# In[12]:


second_per_hour = 60*60
print(second_per_hour)


# Ans3)

# In[13]:


minutes_per_hour = 60*60
print(second_per_hour*24)


# Ans4)

# In[5]:


seconds_per_day = 24*60*60
print(seconds_per_day)


# Ans5)

# In[14]:


print(seconds_per_day/second_per_hour)


# Ans6)

# In[16]:


print(seconds_per_day//second_per_hour, end='')
print(' -> yes this values agree with the floating point value from the previous question')


# Ans7)

# In[18]:


def genPrimes():
    n = 0
    while True :
        if n == 2 or n == 3:
            yield n
        elif ((n-1)%6 == 0 or (n+1)%6 ==0) and n !=1:
            yield n
        n = n+1
        
output =genPrimes()
for ele in range(5):
    print(next(output))

