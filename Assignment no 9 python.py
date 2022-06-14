#!/usr/bin/env python
# coding: utf-8

# Ans1) The relative path is the path to some file with respect to your current working directory.(PWD)
# For example: if Absolute path to a file called stuff.txt is: C:/users/admin/docs/stuff.txt if my PWD is C:/users/admin/ , then the relative path to stuff.txt would be: docs/stuff.txt
# Note: PWD + relative path = absolute path.

# Ans2)In Linux based systems the absolute path starts with /. 
# Where as in Windows based systems absolute path starts with C:

# Ans3) The os.getcwd() method tells us the location of current working directory (CWD).  
# Whereas os.chdir() method in Python used to change the current working directory to specified path. These functions are similar to linux commands pwd and cd.

# Ans4)The . Represents the Current Directory Whereas .. Represents the Parent Directory of the Current Directory
# For Example: if the below path is my absolute path:
# C:\\Users\\vishnu\\Documents\\iNeuron-Assignments\\Python Basic Assignment
# Then . represents the path C:\\Users\\vishnu\\Documents\\iNeuron-Assignments\\Python Basic Assignment
# Where as .. represents the path C:\\Users\\vishnu\\Documents\\iNeuron-Assignments

# Ans5)For C:\bacon\eggs\spam.txt
# The dir name is C:\\bacon\\eggs
# The Base name is spam.txt.

# In[1]:


import os
path = r'C:\bacon\eggs\spam.txt'
print(os.path.dirname(path))
print(os.path.basename(path))


# Ans6) A file can be Accessed in python using open() function. open function takes two arguments filename and mode of operation (optional). if mode is not provided the default mode of opening is read mode.
# So, the syntax being: open(filename, mode)-:
# 
# 1)‘r’ – Read Mode: This is the default mode for open(). The file is opened and a pointer is positioned at the beginning of the file’s content.
# 2)‘w’ – Write Mode: Using this mode will overwrite any existing content in a file. If the given file does not exist, a new one will be created.
# 3)‘r+’ – Read/Write Mode: Use this mode if you need to simultaneously read and write to a file.
# 4)‘a’ – Append Mode: With this mode the user can append the data without overwriting any already existing data in the file.
# 5)‘a+’ – Append and Read Mode: In this mode you can read and append the data without overwriting the original file.
# 6)‘x’ – Exclusive Creating Mode: This mode is for the sole purpose of creating new files.
# Use this mode if you know the file to be written doesn’t exist beforehand.

# Ans7) Using this mode will overwrite any existing content in a file. If the given file does not exist, a new one will be created.

# Ans8)The main difference is that read() will read the whole file at once and then print out the first characters that take up as many bytes as you specify in the parenthesis
# a)Whereas the readline() that will read and print out only the first characters that take up as many bytes as you specify in the parenthesis. You may want to use readline() when you're reading files that are too big for your RAM.
# b)The read() would treat each character in the file separately, meaning that the iteration would happen for every character.
# c)The readline() function, on the other hand, only reads a single line of the file. This means that if the first line of the file were three lines long, the readline() function would only parse (or iterate/operate) on the first line of the file.

# Ans9)The Data Structure contains key and values it represents dictionary.
