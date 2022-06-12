#!/usr/bin/env python
# coding: utf-8

# Ans1) The re.compile() is the feature responsible for generation of Regex objects.

# In[4]:


import re
x = re.compile("some_random_pattern")
type(x)
print(x)


# Ans2) Regular expressions use the backslash character ('\') to indicate special forms (Metacharacters) or to allow special characters (speical sequences) to be used without invoking their special meaning. This collides with Python’s usage of the same character for the same purpose in string literals. Hence, Raw strings are used (e.g. r"\n") so that backslashes do not have to be escaped.

# Ans3) The return value of re.search(pattern,string) method is a match object if the pattern is observed in the string else it return a None.

# Ans4)  For Matched items group() methods returns actual strings that match the pattern.

# In[26]:


import re
match = re.search('ineuron', 'Ineuron Full Stack Data Science Program', flags=re.IGNORECASE)
print('Output:',match.group())


# Ans5)  In the Regex r'(\d\d\d)-(\d\d\d-\d\d\d\d)' the zero group covers the entire pattern match where as the first group cover (\d\d\d) and the second group cover (\d\d\d-\d\d\d\d).

# In[54]:


# Example 
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 222-234-4456.')
print(mo.groups()) # Prints all groups in a tuple format
print(mo.group())  # Always returns the fully matched string 
print(mo.group(1)) # Returns the first group
print(mo.group(2)) # Returns the second group


# Ans6) The \. \( and \) escape characters in the raw string passed to re.compile() will match actual parenthesis characters.

# In[53]:


# Example 
import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (222) 333-4333.')
print(mo.group())


# Ans7) If the regex pattern has no groups, a list of strings matched is returned. if the regex pattern has groups, a list of tuple of strings is returned.

# In[52]:


# Example 
import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.findall('My phone number is (222) 333-4333.')
print(mo)

# Example Program
import re
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.findall('My number is 789-987-4242.')
print(mo) # Prints all groups in a tuple format


# Ans8) In Standard Expressions | means OR operator.

# Ans9)  In regular Expressions  ? characters represents zero or one match of the preceeding group.

# Ans10) In Regular Expressions, * Represents Zero ore more occurances of the preceeding group, whereas + represents one or more occurances of the preceeding group.
# 
# 

# In[43]:


import re
match_1 = re.search("Bat(wo)*man","Batman returns")
print(match_1)
match_2 = re.search("Bat(wo)+man","Batman returns")
print(match_2)


# Ans11) The {4} means that its preceeding group should repeat 4 times.  
#  Where as {4,5} means that its preceeding group should repeat mininum 4 times and maximum 5 times inclusively.

# Ans12) The \d,\w and \s are special sequences in regular expresssions in python:
# 
# 1) \w – Matches a word character equivalent to [a-zA-Z0-9_].
# 2) \d – Matches digit character equivalent to [0-9].
# 3) \s – Matches whitespace character (space, tab, newline, etc.).

# Ans14) The .* is a Greedy mode, which returns the longest string that meets the condition. Whereas .*? is a non greedy mode which returns the shortest string that meets the condition.

# Ans15) The Synatax is Either [a-z0-9] or [0-9a-z].

# Ans16) We can pass re.IGNORECASE as a flag to make a noraml expression case insensitive.

# Ans17) The Dot . character matches everything in input except newline character .. By passing re.DOTALL as a flag to re.compile(), you can make the dot character match all characters, including the newline character.

# Ans18) The Ouput will be 'X drummers, X pipers, five rings, X hen'.

# In[47]:


import re
numReg = re.compile(r'\d+')
numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')


# Ans19) The re.VERBOSE will allow to add whitespace and comments to string passed to re.compile().

# Ans20)

# In[48]:


import re
pattern = r'^\d{1,3}(,\d{3})*$'
pagex = re.compile(pattern)
for ele in ['42','1,234', '6,368,745','12,34,567','1234']:
    print('Output:',ele, '->', pagex.search(ele))


# Ans21)  The pattern = r'[A-Z]{1}[a-z]*\sWatanabe'.

# In[50]:


import re
pattern = r'[A-Z]{1}[a-z]*\sWatanabe'
namex = re.compile(pattern)
for name in ['Haruto Watanabe','Alice Watanabe','RoboCop Watanabe','haruto Watanabe','Mr. Watanabe','Watanabe','Haruto watanabe']:
    print('Output: ',name,'->',namex.search(name))


# Ans22) The pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'

# In[51]:


import re
pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'
casex = re.compile(pattern,re.IGNORECASE)
for ele in ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.','RoboCop eats apples.'
,'ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']:
    print('Output: ',ele,'->',casex.search(ele))


# Ans13) The \D, \W and \S are special sequences in regular expresssions in python:
# 
# 1) \W – Matches any non-alphanumeric character equivalent to [^a-zA-Z0-9_].
# 2) \D – Matches any non-digit character, this is equivalent to the set class [^0-9].
# 3) \S – Matches any non-whitespace character.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




