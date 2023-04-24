# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 20:06:01 2023

@author: Amara
"""

# 1, My daily_quotes function
#import the 'random' module in order to use the random.randint() function.

import random

def daily_quotes(name):
        affirmations = {1: 'God loves you', 2: 'You are doing great!', 3: "Don't give up!", 
                        4: 'The joy of the lord is your strength', 5:"You are engraved in God's palm",
                        6:"Lines are fallen for you in pleasant places", 7:"God's got you",
                        8:"You have an excellent spirit", 9:"The lord is your shepherd"}

#use the i variable to select a random quote from the dictionary using square bracket notation [].    
        i = random.randint(1, len(affirmations))

#use the format method to substitute the name parameter into the output message.    
        return f"{name}, {affirmations[i]}"            # '-1 since index usually starts from 0'

if __name__ == "__main__":                             # allow for import into scripts without running
    print(daily_quotes("Amara")) 
   


print('\n')


# 2, My multiply_num function

def multiply_num(num1, num2):                        # define function
    multiply = num1 * num2
    return multiply

if __name__ == "__main__":                           # allow for import into scripts without running
    print(multiply_num(700,4988))                    # call function with arguments

    
    
    

    
    

    
    
    
    
    
    
    
