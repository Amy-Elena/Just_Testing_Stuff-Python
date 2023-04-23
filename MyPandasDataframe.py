# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:05:24 2023

@author: Amara Igboanugo
"""
# Import pandas package
import pandas as pd

#Create a DataFrame using Dictionary of lists
print('--- Dictionary of lists')
print()
food_dict_of_lists = {"Fruits":pd.Series(data=['apple','mango','lemon','orange']), 
        "Vegetables":pd.Series(data=['cucumber','carrot','cabbage','spinach']),
        "Spices":pd.Series(data=['thyme','ginger','garlic','cinnamon'])}

food = pd.DataFrame(food_dict_of_lists)
print(food)

print()
#Create a DataFrame using List of dictionaries
print('--- List of dictionaries')
print()
food_list_of_dicts = [{'Fruits':'apple', 'Vegetables':'cucumber', 'Spices':'thyme'},
                      {'Fruits':'mango', 'Vegetables':'carrot', 'Spices':'ginger'},
                      {'Fruits':'lemon', 'Vegetables':'cabbage', 'Spices':'garlic'},
                      {'Fruits':'orange', 'Vegetables':'spinach', 'Spices':'cinnamon'}]

food2 = pd.DataFrame(food_list_of_dicts)
print(food2)

print()
#Add new rows to a DataFrame
#New row 1 using .loc()
print('--- Add new row')
print()
food2.loc[4] = ['pineapple', 'lettuce', 'nutmeg']
print(food2)

print()
#New row 2 using .concat()
print('--- Add another new row')
print()
food_row = pd.DataFrame({"Fruits": ['banana'],"Vegetables": ['tomatoes'], "Spices": ['cumin']},
                        index=[5])

food2 = pd.concat([food2, food_row])
print(food2)

print()
#Rename a column, and multiple columns
#Rename a column using rename()
print('--- Rename one column')
print()
food2.rename(columns = {'Vegetables':'Veggies'}, inplace = True)
print(food2)

print()
#Rename multiple columns using .set_axis()
print('--- Rename multiple columns')
print()
food2.set_axis(['Produce', 'Veggies', 'Herb&Spice'], axis='columns', inplace=True)
print(food2)

print()
#Rename row index, and multiple row indexes
#Rename row index using .rename()
print('--- Rename row index')
print()
food2 = food2.rename(index={1: 'i'})
print(food2)

print()
#Rename multiple row indexes using .rename()
print('--- Rename multiple row indexes')
print()
food2 = food2.rename(index={1: 'i', 2: 'ii', 3: 'iii', 4:'iv', 5:'v'})
print(food2)

print()
#Delete rows
#Deleting rows using .drop()
print('--- Delete rows')
print()
food3 = food2.drop(['iv','v'])
print(food3)

print()
#Delete columns
#Deleting columns using .drop()
print('--- Delete columns')
print()
food4 = food3.drop(columns='Herb&Spice')
print(food4)

print()
#Switch column index (change the index position of columns)
#Using .pop() and .insert()
print('--- Pop column indexes')
print()
food4 = food3.pop('Veggies')
print(food4)

print()
print('--- Insert in new index position')
print()
food3.insert(0, 'Veggies',food4)
print(food3)
























