#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[4]:


def guess_me(guess_me):
    if guess_me < 7:
        print('too low')
    elif guess_me > 7:
        print('too high')
    else:
        print('just right')
guess_me(guess_me=7)
guess_me(guess_me=5)
guess_me(guess_me=20)


# Ans2)

# In[5]:


guess_me = 7
start = 1
while True :
    if start < guess_me:
        print('too low')
    elif start  == guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    start +=1
        
        


# Ans3)

# In[7]:


in_list = [3,2,1,0]
for ele in in_list:
    print(ele)


# Ans4)

# In[8]:


print([x for x in range(10+1) if x%2==0])


# Ans5)

# In[10]:


print(dict([(x, pow(x,2)) for x in range(10)]))


# Ans6)

# In[11]:


print({x for x in range(10) if x%2 !=0})


# Ans7)

# In[12]:


gen_com = ('Got_ ' +str(x) for x in range(10))
for ele in gen_com:
    print(ele, end='')


# Ans8)

# In[13]:


def good():
    x = ['Harry', 'Ron', 'Hermione']
    return x
print(good())


# Ans9)

# In[32]:


def get_odds():
    output = []
    for ele in range(10):
        if ele%2 != 0:
            output.append(ele)
    yield output

next(get_odds())[2]


# Ans10)

# In[33]:


class OopsException(Exception):
    pass
def test(input):
    if input < 0:
        raise OopsException(a)
try :
    test(-100)
except Exception as e:
    print('Caught in Oops ->', e)


# Ans11)

# In[40]:


titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
output = dict(zip(titles,plots))
print(output)

