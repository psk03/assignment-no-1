#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[2]:


class Thing:
    pass
print(Thing)

example = Thing()
print(example)


# Ans2)

# In[3]:


class Thing2:
    letters = 'abc'
    
print(Thing2.letters)


# Ans3)

# In[7]:


class Thing3:
    def __init__(self):
        self.letters = 'xyz'
        
try:
    print(Thing3.letters) 
except:
    my_thing = Thing3()
    print(my_thing.letters)


# Ans4)

# In[8]:


class Element:
    def __init__(self, name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number
        
my_elemens = Element('Hydrogen', 'H', 1)


# Ans5)

# In[13]:


custom_dict = {'name':'Hydrogen','symbol':'H','number':1}
print(custom_dict)

# Method 1
hydrogen = Element(*custom_dict.values())
print('Using Method #1 ->',hydrogen.name,hydrogen.symbol,hydrogen.number, sep='\t')

# Method 2
hydrogen = Element(**custom_dict)
print('Using Method #2 ->',hydrogen.name,hydrogen.symbol,hydrogen.number, sep='\t')


# Ans6)

# In[14]:


class Element:
    def __init__(self, name , symbol , number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name, self.symbol, self.number)
        
hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()


# Ans7)

# In[21]:


print(hydrogen)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number      
    def __str__(self):
        return f'{self.name} {self.symbol} {self.number}'
        
Hydrogen = Element('Hydrogen','H',1)
print(Hydrogen)


# Ans8)

# In[22]:


class Element:
    def __init__(self,name,symbol,number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_symbol(self):
        return self.__symbol
    
    @property
    def get_number(self):
        return self.__number
    
hydrogen = Element('Hydrogen','H',1)
print(hydrogen.get_name)
print(hydrogen.get_symbol)
print(hydrogen.get_number)


# Ans9)

# In[23]:


class Bear:
    def eats(self):
        print('berries')
class Rabbit:
    def eats(self):
        print('clover')
class Octothorpe:
    def eats(self):
        print('campers')
        
bear = Bear()
rabbit = Rabbit()
octothrope = Octothorpe()

bear.eats()
rabbit.eats()
octothrope.eats()


# Ans10)

# In[24]:


class Laser:
    def does(self):
        return 'disintegrate'
class Claw:
    def does(self):
        return 'crush'
class Smartphone:
    def does(self):
        return 'ring'
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = Smartphone()
    def does(self):
        print(self.laser.does(),self.claw.does(),self.smartphone.does())
        
r2d2 = Robot()
r2d2.does()

