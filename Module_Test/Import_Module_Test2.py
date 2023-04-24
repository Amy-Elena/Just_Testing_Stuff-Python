# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 09:51:51 2023

@author: Amara
"""

from my_food_class import Food

my_yum = Food('jollof rice', 'slushie')    # created a new instance of the class with object 'my_yum'

my_yum.menu()                              # called a method in the 'Food' class, 'menu()'

print(my_yum.main_course)                # accessed an attribute 'main course', in the class through the object
print(my_yum.dessert_option)



