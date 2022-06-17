#!/usr/bin/env python
# coding: utf-8

# Ans1

# In[2]:


spam = -10
assert spam >=0, 'Variable Spam should not be a -ve number'


# Ans2)

# In[3]:


def raise_assert(egg,bacon):
    egg = egg.upper()
    bacon = bacon.upper()
    assert not(egg == bacon), 'Eggs/Bacon should not be same, which are same now'


# In[4]:


raise_assert('hello','HELLO')


# In[5]:


raise_assert('goodbye','GOODbye')


# Ans3)

# In[6]:


def assert_always():
    assert False, 'Always Shows Assertion Error'
assert_always()


# Ans4)

# In[7]:


import logging
logging.basicConfig(filename = 'application_log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# Ans5)

# In[8]:


import logging
logging.basicConfig(filename = 'application_log.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug("Data Inserted Successfully")
logging.debug('Connection Closed Successfully')


# In[9]:


file = open("./application_log.txt","r")
for record in file.readlines():
    print(record)


# Ans6)The Five levels of Logging provided by python's logging module are CRITICAL(50), ERROR(40), WARNING(30), INFO(20, DEBUG(10), NOTSET(0).

# Ans7)

# In[10]:


logging.disable = True


# Ans8) Post devlopment of your code, you can disable logging messages without removing the logging function, whereas you need to manually remove print() statements, which is tedious activity. and also print is used when you want to display any particular message or help whereas logging is used to record all events like error, info, debug messages, timestamps.

# Ans9)The Differences between Step Over, Step In, Step Out buttons in debugger are:
# 
# 1)Step in - Step In button will cause the debugger to execute the next line of code and then pause again.
# 2)Step Over - Step Over button will execute the next line of code, similar to the Step In button. However, if the next line of code is a function call, the Step Over button will “step over” the code in the function. The function’s code will be executed at full speed, and the debugger will pause as soon as the function call returns.
# 3)Step out - Step Out button will cause the debugger to execute lines of code at full speed until it returns from the current function.

# Ans10) This will cause the program to continue running normally, without pausing for debugging untill it terminates or reaches a breakpoint.

# Ans11) Breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line.
