#!/usr/bin/env python
# coding: utf-8

# Ans1)RGBA is a four-channel format containing data for Red, Green, Blue, and an Alpha value. Where Alpha Represents the Opacity.

# Ans2)ImageColor.getcolor() gives rgba value of any image.

# Ans3)A box tuple is a tuple value of four integers: the left-edge x-coordinate, the top-edge y-coordinate,the width, and the height, respectively.

# Ans4

# In[13]:


#Example Program
from PIL import Image
pic = Image.open('pranav 1.jpg')
print(f'Width, Height -> {pic.size}') # Approach 1
print(f'Width, Height -> {pic.width},{pic.height}') # Approach 2
width,height = pic.size
print(f'Width, Height -> {width},{height}') # Approach 3


# Ans5)

# In[16]:


#example
from PIL import Image
img = Image.open('pranav 1.jpg')
new_img = img.crop((0,50,50,50))


# Ans6)

# In[22]:


#example
from PIL import Image
pic = Image.open('pranav 1.jpg')
pic.save('pranav 2.jpg')


# Ans7)  The Pillows ImageDraw module contains Shape drawing methods.

# Ans8)  ImageDraw objects have shape-drawing methods such as point(), line(), or rectangle().They are returned by passing the Image object to the ImageDraw.Draw() function.
