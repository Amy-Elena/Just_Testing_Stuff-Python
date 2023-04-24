# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 09:15:10 2023

@author: Amara
"""

# Import the Food class from my_food_class.py
from my_food_class import Food

# Create an instance of the Food class
my_menu = Food('pasta', 'cake')

# Call the menu method of the Food class
my_menu.menu()

# Access the main_course and dessert_option attributes of the Food class
print(my_menu.main_course)
print(my_menu.dessert_option)
