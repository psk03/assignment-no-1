#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[4]:


in_dict = {1:'Sambhajinagar', 2:'Pune', 3:'Solapur', 4:'Mumbai', 5:'Riagad', 6:'Jalna'}
print(in_dict.values())
print(f'Unique Values: {list(set(in_dict.values()))}')


# Ans2)

# In[5]:


in_dict = {'Sugar':70,'Turdal':100,'Soyabean':80,'Oats':60}
print('Sum of All items:' , sum(in_dict.values()))


# Ans3)

# In[6]:


course_details = {
    'course_name': 'Fsds'   
}

instructors = {
    'course_instructors':['Sudhanshu Kumar', 'Krish Naik']
    
}
course_details.update(instructors)
print(course_details)


# Ans4

# In[8]:


in_list = [('A',10),('B',20),('C',30),('D',40),('E',50),('F',60),('G',70),('H',80),('I',90),('J',100)]


dict(in_list)


# Ans5)

# In[9]:


from collections import OrderedDict
dict_one = OrderedDict({'Apple':'Iphone','Microsoft':'Windows','Google':'chrome'})
print('dict_one',dict_one)
dict_two = {'Tesla':'SpaceX'}
dict_one.update(dict_two)
print('dict_one',dict_one)
dict_one.move_to_end('Tesla',last=False)
print('dict_one',dict_one)


# Ans6)

# In[10]:


from collections import OrderedDict

initial_list = {'a': 1000, 'f': 200, 'd': 300, 'c': 400, 'b': 500, 'e': 600}
print(initial_list)

final_list = OrderedDict(dict(sorted(initial_list.items())))
print(final_list)


# Ans7)

# In[12]:


d_items = {'Mango':100,'PineApple':22,'Banana':60,'Grape':13}

def sort_dict(in_dict,sort_type):
    if sort_type == 'key':
        print(dict(sorted(in_dict.items(), key=lambda x:x[0], reverse=False)))
    else:
        print(dict(sorted(in_dict.items(), key=lambda x:x[1], reverse=False)))
        
sort_dict(d_items,'key')        
sort_dict(d_items,'value')

