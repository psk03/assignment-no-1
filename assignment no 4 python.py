#!/usr/bin/env python
# coding: utf-8

# Ans1)The epmty list is represented by [ ] is a list that contains no items.

# Ans2)The indexing start from '0' so spam[2] will be at zero position.
# spam[2]='hello'.
# 

# In[28]:


#example

spam=[2,4,6,8,10]
print(spam)
spam[2] ='hello'
print(spam)
    


# Ans3)

# In[10]:


spam =['a','b','c','d',]
print("spam[int(int('3'*2)//11)]) ->" , spam[int(int('3'*2)//11)])


# Ans4)The spam[-1] returns 'd', whereas list supports the negative indexing.
# 

# Ans5)Spam[:2] returns all the element in a list spam from 0 to 2 excluding 2

# In[29]:


# example

print(spam)
print(spam[:2])


# Ans6)The value of bacon.index('cat') is 1.

# In[30]:


bacon = [3.14,'cat', 11,'cat',True]
print("bacon.index('cat') ->", bacon.index('cat'))


# Ans7)The append method is used to add new elements to the end of the list.

# In[18]:


#example

print(bacon)
bacon.append(99) 
print(bacon)


# Ans8)The bacon.remove('cat') can be remove by remove method.

# In[31]:


print(bacon)
bacon.remove('cat')
print(bacon)


# Ans9)The operators for the list concatenations is '+' , while the operators for replication is '*'.

# In[32]:


#example

list1 = ['physics', 'chemistry', 'maths', 'socialscience']
list2 = ['algebra', 'gometry','hindi','english']
print(list1 + list2)     #concatenation
print(list2*2)           #replication


# Ans10)The list method append() is used to add the values only at the end of list.
# The list method insert() can be used to add values anywhere in the list.

# In[33]:


# example

list =[1,2,3,4,5]
list.append(6)
print(list)
list.insert(2,'Demo')
print(list)


# Ans11)The del statement and the remove() method are two ways to remove values from a list.

# Ans12)Both lists and strings can be passed to len() function, have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.

# Ans13): Lists are Mutable, Indexable and Slicable. they can have values added, removed, or changed.
# Tuples are Immutable but Indexable and Slicable, the tuple values cannot be changed at all. 
# Also tuples are represented using parentheses (), while lists use the square brackets [].

# Ans14)To typle a tuple value that only contains integer 42 is with comma.The comma is mandatory.Otherwise it is considered as a int by a python interpreter.

# In[34]:


n = (42)
m = (42,)
print(type(n))
print(type(m))


# Ans15)The tuple() and list() functions, respectively are used to convert a list to tuple and vice versa.

# Ans16)They contain references to list values.

# Ans17)The copy.copy() function will do a shallow copy of a list.
# While the copy.deepcopy() function will do a deep copy of a list. That is only copy.deepcopy() will duplicate any lists inside the list.
