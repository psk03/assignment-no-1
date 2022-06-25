#!/usr/bin/env python
# coding: utf-8

# Ans1)

# In[1]:


def checkDisariumNumber():
    in_num = input('Enter a Number: ')
    sum = 0
    for item in range(len(in_num)):
        sum = sum + int(in_num[item])**(item+1)
    if sum == int(in_num):
        print(f'{in_num} is a Disarium Number')
    else:
        print(f'{in_num} is a Not Disarium Number') 

checkDisariumNumber()
checkDisariumNumber()
    


# Ans2)

# In[3]:


def printDisariumNumbers(start=0,end=100):
    output_num = []
    for number in range(start,end+1):
        sum = 0
        for item in range(len(str(number))):
            sum = sum + int(str(number)[item])**(item+1)
        if sum == number:
            output_num.append(number)
    return output_num

printDisariumNumbers(1,1000)


# Ans3

# In[1]:


def checkHappyNumber():
    in_num = input('Enter a Number: ')
    in_num_duplicate = in_num
    trackNumber = set()   
    while True:
        if in_num != '1' and str(in_num) not in trackNumber:
            trackNumber.add(in_num)
            sum = 0
            for ele in range(len((in_num))):
                sum = sum + int(in_num[ele])**2
            in_num = str(sum)
        elif str(in_num) in trackNumber:
            print(f'{in_num_duplicate} is not a Happy Number')
            break
        else:
            print(f'{in_num_duplicate} is a Happy Number')
            break

checkHappyNumber()
checkHappyNumber()


# Ans4

# In[2]:


def checkHappyNumber(start=0,end=100):
    happyNumbersList = []
    for in_num in range(start,end+1):
        in_num = str(in_num)
        inum_holder = in_num
        trackNumber = set()   
        while True:
            if in_num != '1' and str(in_num) not in trackNumber:
                trackNumber.add(in_num)
                sum = 0
                for ele in range(len((in_num))):
                    sum = sum + int(in_num[ele])**2
                in_num = str(sum)
            elif str(in_num) in trackNumber:
                break
            else:
                happyNumbersList.append(int(inum_holder))
                break
    print(f'The Happy Numbers between {start} and {end} are {happyNumbersList}')
    
checkHappyNumber(0,100)


# Ans5)

# In[1]:


def checkHarshadNumber():
    in_num = input('Enter a Number: ')
    sum = 0
    for item in range(len(in_num)):
        sum = sum + int(in_num[item])
    if int(in_num)%sum == 0:
        print(f'{in_num} is a Harshad Number')
    else:
        print(f'{in_num} is a Not Harshad Number')
        
checkHarshadNumber()
checkHarshadNumber()


# Ans6)

# In[2]:


def printPronicNumbers(start=0,end=100):
    outputlist = []
    for ele in range(start,end+1):
        outputlist.append((ele)*(ele+1))
    print(outputlist)
    
printPronicNumbers()
    

