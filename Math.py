#!/usr/bin/env python
# coding: utf-8

# In[2]:


#function for the house
def calc_sq_footage(length,width):
    return length * width

#user input for home dimensions

house_length=float(input('Enter the length of your house in feet: '))
house_width=float(input('Enter the width of your house in feet: '))

house_sq_footage = calc_sq_footage(house_length,house_width)
print(f'The square footage of the house is {house_sq_footage} square feet.')
      
#function to calculate radius of a circle

def calc_circumference(radius):
    return 2* 3.14 *radius
#user input for circle radius
circle_radius = float(input('Enter the radius of the circle in feet: '))
      
#calculate the circ of circle
circle_circumference = calc_circumference(circle_radius)
print(f'The circumference of the circle is {circle_circumference} feet.')


# In[ ]:




