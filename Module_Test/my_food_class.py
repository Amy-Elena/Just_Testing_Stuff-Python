# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:02:49 2023

@author: Amara
"""




class Food:                                              # define class
    def __init__(self, main_course, dessert_option):     # "__init__" constuctor method with every class
        self.main_course = main_course                   # "self" reference to object method is operating on               
        self.dessert_option = dessert_option             # 'main_course, dessert_option' instance attributes as args
        
    def menu(self):                                      # define method for class 
        print(f"Your main course for today is {self.main_course} and dessert is {self.dessert_option}")
        
if __name__ == '__main__':                               # wrap in '__main__' so it won't run if imported as a module
    
    my_menu = Food('fried rice', 'ice cream')            # create an object (instance of the class), pass arguments

    my_menu.menu()                                       # call the method of the object

    print(my_menu.main_course)                           # access attribute without calling method
    print(my_menu.dessert_option) 





# option 2
'''
class Food:                                              
    def __init__(self, main_course= 'fried rice', dessert_option= 'ice cream'): 
        self.main_course = main_course                                 
        self.dessert_option = dessert_option             
        
    def menu(self):                                      # define method for class 
        print(f"Your main course for today is {self.main_course} and dessert is {self.dessert_option}")
        

my_menu = Food()                

my_menu.menu()                                           

      
print(my_menu.main_course)                               
print(my_menu.dessert_option) 
'''













                       
