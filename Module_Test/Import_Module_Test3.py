# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 10:04:24 2023

@author: Amara
"""

         
import my_food_class     

# have to reference 'my_food_class' to call 'Food' (or use 'from my_food_class import Food')

my_delish = my_food_class.Food('plantain & eggs', 'smoothie')        # Create an instance of the Food class

# Call the menu method of the Food class with the object created
my_delish.menu()

# Access the main_course and dessert_option attributes of the Food class
print(my_delish.main_course)
print(my_delish.dessert_option)
