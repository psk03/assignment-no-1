#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[3]:


class div_generator:
    def __init__(self,in_num):
        self.in_num = in_num
    def get_numbers(self):
        for ele in range(0,self.in_num+1):
            if ele%7 == 0:
                yield ele
output = div_generator(350)
for ele in output.get_numbers():
    print(ele,end=' ')


# Ans2)

# In[8]:


def checkFrequency():
    in_string = input("Enter the Input String: ")
    frequency = {}
    for ele in in_string.split(" "):
        if(frequency.get(ele) == None):
            frequency[ele] = 1
        else:
            frequency[ele] += 1 
    for ele in sorted(frequency):
        print(f'{ele}:{frequency[ele]}',end=" ")
checkFrequency()


# Ans3)

# In[11]:


class Person():
    def getGender():
        pass
class Male(Person):
    def getGender():
        print("Male")

class Female(Person):
    def getGender():
        print("Female")
        
Male.getGender()
Female.getGender()


# Ans4)

# In[16]:


def generateSentences():
    subject = ['I','You']
    verb = ['Play','Love']
    object = ['Hockey','Football']
    for s in subject:
        for v in verb:
            for o in object:
                print(f'{s} {v} {o}')
                
generateSentences()


# Ans5)

# In[20]:



def compress(in_string):
    output = in_string[0]
    count = 1
    for ele in range(len(in_string)-1):
        if in_string[ele] == in_string[ele+1]:
            count +=1
        else:
            if count > 1:
                output += str(count)
            output += in_string[ele+1]
            count = 1
    if count > 1:
        output += str(count)            
    print(output)


def decompress(in_string):
    output = ''
    for ele in range(len(in_string)):
        if in_string[ele].isdigit():
            output += output[-1]*(int(in_string[ele])-1)
        else:
            output += in_string[ele]
    print(output)
    
        
compress("hello world!hello world!hello world!hello world!")
decompress("hel2o world!hel2o world!hel2o world!hel2o world!")

compress('I love my India')
decompress('I love my Pet')
                     


# Ans6)

# In[21]:


sorted_list = [1,2,3,4,5,6,7,8,9,10]
def binary_search(in_list,in_num):
    low = 0
    high = len(in_list)-1
    while low <= high:
        mid = high+low//2
        if in_list[mid] < in_num:
            low = mid+1
        elif in_list[mid] > in_num:
            high = mid-1
        else:
            return mid
    else:
        return 'Input Element not in the list'
    
print(binary_search(sorted_list,8))
print(binary_search(sorted_list,100))


# In[ ]:




