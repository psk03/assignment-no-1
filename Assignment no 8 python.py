#!/usr/bin/env python
# coding: utf-8

# Ans1) The PyInputPlus is not the part of the Python Standard Library,it needs to be installed explicitly using the command !pip install PyInputPlus. 

# Ans2) We can import the module with import pyinputplus as pyip so that you can enter a shorter name when calling the module's functions.

# Ams3) The inputInt() function accepts an integer value.This can also takes additional parameters min,max,greaterThan,and lessThan for bounds and it always return an int.
# 
# Whereas inputFloat() function accepts a floating-point numeric value.
# This also takes additional min,max,greaterThan and lessThan parameters and always return a float.

# Ans4) PyInputPlus module provies a function called as inputInt() which only return only integer values inorder to restrict the input between 0 and 99.
# We can use parameter like min & max to ensure that user enters the values between the defined range only.

# 
# import pyinput as pyip
# wholenumber = pyip.inputInt(prompt='Enter a number:', min=0, max=100)
# print(wholenumber)

# Ans5) The allowRegexes and BlockRegexes are keyword that we can use to take list of regular expression string to determine what the pyinputplus function will reject or accept valid input.

# Ans7) The statement inputStr(limit=3) will throw two exceptions ValidationException and RetryLimitException.
# The first exception is thrown because blank values are not allowed by inputStr() function by default. it we want to consider blank values as valid input, we have to set blank=True.
# 
# The second exception is occured because we have reached the max limit we have specified by using limit parameter. inorder to avoid this exception we can use default parameter to return a default value when max limit is reached.

# Ans8)  The default parameter is set to hello, after blank input is entered three times instead of raising RetryLimitException exception. the function will return hello as response to the calling function.
