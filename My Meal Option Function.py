# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 20:21:34 2023

@author: Amara
"""

# Solving the 'Meal Option Function' finally 
"""
INSTRUCTION:
- Write a python function that suggests various meal options depending on the locations in the 
  country and time of the day (morning, afternoon, evening). 

- You can get as creative with your function as you would like. 

- Your function must incorporate the use of arguments and should include a least one type of loop. 

- You can make use of data structures you see necessary for your solution. 

- Your function should take inputs like customer name, location, and time of the day, 
  and also ask if the customer would like to eat some more food before terminating the program. 
"""

# Create a dictionary of food options for each region 
menu = {'East_breakfast': ["Okpa & Pap", "Moi-Moi & Custard"], 
        'West_breakfast':["Akara & Custard", "Beans & Pap"], 
        'North_breakfast': ["Masa & Millet", "Beans & Fura"], 
        'South_breakfast': ["Moi-Moi & Pap", "Plantain & Pepper Sauce"], 
        'East_lunch': ["Oha Soup & Eba", "Abacha & Fried Fish"], 
        'West_lunch': ["Jollof Rice", "Amala & Ewedu"], 
        'North_lunch': ["Tuwo & Okro Soup", "Tuwo & Soup"], 
        'South_lunch': ["Fisherman Soup & Starch", "Rice & Light Stew"],
        'East_dinner': ["Oha Soup & Fufu", "Ukwa"], 
        'West_dinner': ["Stewed Beans", "Yam Porridge"], 
        'North_dinner': ["Suya Noodles", "Coconut Rice"], 
        'South_dinner': ["Banga Rice", "Bole & Fish"]}

# Create a list of the regions and initialize the Value of i to start at 0
region = ['East', 'West', 'North', 'South']
i = 0

# Create of list of time of the day(Time 0f Day) and initialize the Value of i to start at 0
TOD = ['Morning', 'Afternoon', 'Evening']
i = 0


# Define the meal option finction
def yummy(location, time):  #The entries for the parameters inside the () determine the output
    """
    'yummy' Function:
    Tells user meal suggestions for breakfast, lunch and dinner inspired by regional cuisines.

    Extended Description of Function.

    Parameters:
    menu_option(dict): The menu options for breakfast, lunch and dinner for each region
    region(list): A list of the regions for the menu
    time_of_day(list): A list of time of the day
    name(str): Name of the user
    location(str): User inputs the state
    time_of_day(str): User inputs the time of the day

    Returns:
    Meal idea for breakfast, lunch or dinner depending on region input

    """
    print("yummy suggests Nigerian regional cuisines for breakfast, lunch and dinner.\n")
    
    name = (input("\nHi foodie! what is your first name?: ")).title()
    location = (input("\nYour city in Nigeria, is it in the east, west, north or south?: ")).title()
    time = (input("\nGreat! is it morning, afternoon or evening?: ")).title()
    
    if location in region[0] and time == TOD[0]: #list indices must be integers or slicers not string
        return("\n>>>>>> {}! Your breakfast idea is: {}".format(name,menu['East_breakfast'][i]))
    elif location in region[0] and time == TOD[1]:
        return ("\n>>>>>> {}! Your lunch idea is: {}".format(name,menu['East_lunch'][i]))
    elif location in region[0] and time == TOD[2]:
        return ("\n>>>>>> {}! Your dinner idea is: {}".format(name,menu['East_dinner'][i]))
    elif location in region[1] and time == TOD[0]:
        return ("\n>>>>>> {}! Your breakfast idea is: {}".format(name,menu['West_breakfast'][i]))
    elif location in region[1] and time == TOD[1]:
        return ("\n>>>>>> {}! Your lunch idea is: {}".format(name,menu['West_lunch'][i]))
    elif location in region[1] and time == TOD[2]:
        return ("\n>>>>>> {}! Your dinner idea is: {}".format(name,menu['West_dinner'][i]))
    elif location in region[2] and time == TOD[0]:
        return ("\n>>>>>> {}! Your breakfast idea is: {}".format(name,menu['North_breakfast'][i]))
    elif location in region[2] and time == TOD[1]:
        return ("\n>>>>>> {}! Your lunch idea is: {}".format(name,menu['North_lunch'][i]))
    elif location in region[2] and time == TOD[2]:
        return ("\n>>>>>> {}! Your dinner idea is: {}".format(name,menu['North_dinner'][i]))
    elif location in region[3] and time == TOD[0]:
        return ("\n>>>>>> {}! Your breakfast idea is: {}".format(name,menu['South_breakfast'][i]))
    elif location in region[3] and time == TOD[1]:
        return ("\n>>>>>> {}! Your lunch idea is: {}".format(name,menu['South_lunch'][i]))
    elif location in region[3] and time == TOD[2]:
        return ("\n>>>>>> {}! Your dinner idea is: {}".format(name,menu['South_dinner'][i]))
    else:
        return("Oops! you entered the wrong word")

permission = "loop starts"

while permission == "loop starts":
    yummy_options = yummy(location=region, time=TOD)   #Call function, link input to defined parameters
    print("{}\n\n------ Meals are never boring with Yummy! ------".format(yummy_options))
    
    while True:
        check = input("\nDo you want another meal option? (Y:Yes, N:No): ").upper()
        if check == 'Y':
            i += 1
            break
        elif check == 'N':
            print("\nAlright enjoy your meal")
            permission = "loop stops"
            break
        else:
            print("\nThere's something wrong with your input, please try again")
            
    if check == "Y" and i == 2:
           print("Sorry, You have reached the end of the meal options in your location at this time.")
           permission = "loop stops"



















