#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Ans1) There are a total of 4 Operators and 3 Expressions, They are:
Operators: *,-,/,+
Expressions: 'hello', 87.8, 6


# Ans2)
# A Variable is used to store of information, and a String is a type of information you would store in a Variable. A String is a group of characters or a single character usually enclosed in Double quotes " " or single quotes ' '

# Ans3)
# Three fundamental Data types in python are int, float, complex.
# 
# int data type: We can use int data type to represent whole numbers (integral values)
# float data type: We can use float data type to represent floating point values (decimal values)
# complex data type: Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j

# In[1]:


# Example for int data type
int_num=4567
print(int_num, type(int_num))


# In[2]:


# Example for float data type
flo_num=1.2e3
print(flo_num, type(flo_num))


# In[3]:


# Example for Complex data type
com_num=10+1.5j
print(com_num, type(com_num))


# Ans4)  An expression is a combination of values, variables, operators, and calls to functions. Expressions need to be evaluated. If we ask Python to print an expression, the interpreter evaluates the expression and displays the result.

# In[4]:


4*5+20-40 # Is an Expression, The Python Interpreter Evaluates it to 0


# Ans5) An expression is a combination of values, variables, and operators.When we type an expression at the prompt, the interpreter evaluates it, which means that it finds the value of the expression.
# 
# eg- 4*5+20-40 is an example of a statement.
# 
# A statement is a unit of code that has an effect, like creating a variable or displaying a value.When we type a statement, the interpreter executes it, which means that it does whatever the statement says. In general, statements don’t have values.
# 
# eg- variable declaration and assignment are statements because they do not return a value.

# In[5]:


#Example:
4*5+20-40 # Is a Expression
courseName = 'INeuron FullStack DataScience' # Is a Statement
print("Hello World !") # Is a Expression Statement


# Ans6) The variable bacon is set to 22 .The expression bacon + 1 does not reassign the value in bacon (that would the case if the expression is like bacon = bacon + 1 instead of bacon + 1)

# In[6]:


# Example Case#1
bacon=22
bacon+1
print(bacon)


# In[7]:


#Example Case#2
bacon=22
bacon=bacon+1 
print(bacon)


# Ans7) : Both expressions evaluate to the string 'spamspamspam' Where as the first expression follows String Concatentation and the second expression follows String Multiplication.

# In[8]:


print('spam'+'spamspam') # string concatenation
print('spam'*3) # string multiplication


# Ans8)  As per python,Variable names cannot begin with a number. The python rules for naming a variable are :-
# 
# Variable name must start with a letter or the underscore character.
# Variable name cannot start with a number.
# Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, & _ ).
# Variable names are case-sensitive (name, INEURON and ineuron are three different variables).
# The reserved words(keywords) cannot be used naming the variable.

# In[9]:


egg='Ineuron' # Valid variable Initilization
100='hello' # Invalid Variable Initilization
print(egg) #prints the value of egg ie Ineuron
print(100) # Raises a Syntax Error as 100 is not a valid variable name


# Ans9)The int(),float(),and str() functions will evaluate to the integer,floating-point number,string version of the value passed to them.

# In[10]:


# Examples:
print('int(10.0) -> ',int(10.0)) # int() function converts given input to int
print('float(10) -> ',float(10)) # float() function converts given input to float
print('str(10) -> ',str(10)) # str() function converts given input to string


#  Ans10) This cause of error is 99.because 99 is not a string. 99 must be typecasted to a string to fix this error. the correct way is:
# Input: 'I have eaten ' + str(99) + 'burritos.'
# Output: 'I have eaten 99 burritos.'

# In[12]:


print('I have eaten '+str(99)+' burritos')


# In[ ]:




