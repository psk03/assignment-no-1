#!/usr/bin/env python
# coding: utf-8

# Ams1)

# In[8]:


years_list = [ele for ele in range(1997,1997+6)]
print(years_list)


# Ans2)

# In[9]:


print(years_list[3])


# Ans3)

# In[10]:


print(years_list[-1])


# Ans4)

# In[11]:


things = [ele+'ella' for ele in ['mozzar', 'cinder', 'salmom']]
print(things)


# Ans5)

# In[12]:


for ele in range(len(things)):
    if things[ele]  == 'cindrella':
        things[ele]  == things[ele].capitalize()
print(things)


# Ans6)

# In[15]:


suprise_list = ['Groucho', 'Chico', 'Harpo']
print(suprise_list)


# Ans7)

# In[16]:


print(suprise_list[-1].lower()[::-1].capitalize())


# Asn8)

# In[18]:


e2f = {'dog' : 'chien' , 'cat' : 'chat', 'walrus' :'morse'}
print(e2f)


# Ans9)

# In[19]:


print(e2f.get('walrus'))


# Ans10)

# In[21]:


f2e = dict([ele[::-1] for ele in e2f.items()])
print(f2e)


# Ans11)

# In[22]:


print(f2e.get('chien'))


# Ans12)

# In[23]:


print(list(e2f.keys()))


# Ans13)

# In[24]:


life = {
    'animals':{
        'cats':['Henri','Grumpy','Lucy'],
        'octopi':{},
        'emus':{}
    },
    'plants':{},
    'other':{}
}
print(life)


# Ans14)

# In[25]:


print(list(life.keys()))


# Ans15)

# In[27]:


print(list(life['animals'].keys()))


# Ans16)

# In[28]:


print(life['animals']['cats'])

