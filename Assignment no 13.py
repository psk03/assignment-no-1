#!/usr/bin/env python
# coding: utf-8

# Ans1)The Advantages of Excel over CSV are:
# a)Excel (XLS and XLSX) file formats are better for storing and analysing complex data.
# b)An Excel not only stores data but can also do operations on the data using macros, formulas etc.
# c)CSV files are plain-text files, Does not contain formatting, formulas, macros, etc. It is also known as flat files.

# Ans3) For csv.reader(iterable_file_object), the file objects needed to be opened in read mode mode='r' Whereas for csv.writer(iterable_file_object) the file objects needed to be opened in write mode mode='w'.

# Ans4)csv.writer class provides two methods for writing to CSV. They are writerow() and writerows(). writerow() method writes a single row at a time. Whereas writerows() method is used to write multiple rows at a time.

# In[24]:


# Example Program
import csv      
fields = ['Name', 'Branch', 'Year', 'CGPA'] #column names 
rows = [ 
            ['Nikhil', 'COE', '2', '9.0'],  # data rows of csv file 
            ['Sanchit', 'COE', '2', '9.1'], 
            ['Ravi', 'IT', '2', '9.3']
       ] 
with open("university_records.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) # creating a csv writer object 
    csvwriter.writerow(fields) # writing the fields 
    csvwriter.writerows(rows) # writing the data rows 


# Ans5)

# Lets take the example of a csv file:
# First Name, Last Name, Age
# Mano, Vishnu, 24
# Vishnu, Vardhan, 21
# Here ',' is Delimiter. We can use any Character as per our needs if required. Similarly Line Terminator comes at end of line by default it is newline and can be changed accourding to Requirement.

# Ans6)loads() method takes a string of JSON data and returns a Python data structure.

# In[25]:


# Example of json.loads() method
import json
my_details_json ='''{
    "Name": "Mano Vishnu",
    "Qualification": "Bachelor of Technology",
    "Stream": "Computer Science and Engineering"
}'''
print(my_details_json)
print(f'Type of my_details_json is {type(my_details_json)}')
my_details = json.loads(my_details_json)
print(my_details)
print(f'Type of my_details is {type(my_details)}')


# Ans7)

# In[26]:


# Example of json.dumps() method
import json
my_details = {
    'Name':'Mano Vishnu',
    'Stream':'Computer Science and Engineering',
    'Qualification':'Bachelor of Technology'
}
print(my_details)
print(f'Type of my_details is {type(my_details)}')
my_details_json = json.dumps(my_details, indent=4, sort_keys=True)
print(my_details_json)
print(f'Type of my_details_json is {type(my_details_json)}')

