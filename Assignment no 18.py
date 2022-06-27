#!/usr/bin/env python
# coding: utf-8

# In[7]:


get_ipython().system('type zoo.py')


# Ans1
# 

# In[8]:


import zoo
zoo.hours()


# Ans2)

# In[10]:


import zoo as menagerie
menagerie.hours()


# Ans3)

# In[11]:


from zoo import hours
hours()


# Ans4

# In[12]:


from zoo import hours as info
info()


# Ans5)

# In[13]:


plain_dict = {'a':1, 'b':2,'c':3}
print(plain_dict)


# Ans6)

# In[14]:


from collections import OrderedDict
fancy = OrderedDict(plain_dict)
print(f'plain_dict -> {plain_dict}')
print(f' fancy -> {fancy}')


# Ans7)

# In[16]:


from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])

