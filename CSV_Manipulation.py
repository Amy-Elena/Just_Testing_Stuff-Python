# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:59:51 2023

@author: Amara
"""

#Import packages
import pandas as pd
import numpy as np
from tabulate import tabulate

#Read csv
df = pd.read_csv("outfile.csv")
print(df.head())
print()

#Use .tabulate() to show all columns
print(tabulate(df.head(), headers='keys', tablefmt='psql'))
print()

#Specify no of rows for head()
print(tabulate(df.head(10), headers='keys', tablefmt='psql'))
print()

#Drop irrelevant columns
df.drop(columns=["Remarks", "Value. Date", "Reference", "Originating Branch"], axis=1, inplace=True)
print(df)
print()

#See no of rows and columns with .len()
print(len(df))
print()

#Drop rows with all zeros
# df.loc[~(df==0).all(axis=1)]
#OR
# df.loc[(df!=0).any(axis=1)]

#Find null rows(for 'Trans Date') using numpy (numpy is better)
#In this case, rows with Trans.date value as zero are irrelevant
null_rows = np.where(pd.isnull(df["Trans. Date"]))[0]
print(null_rows)
print()

#Drop the rows
df.drop(labels=null_rows, inplace=True)
print(df.head())
print()

#Reset index (cos of dropped rows)
df.reset_index(drop=True, inplace=True)
print(df.head())
print()

#Replace commas with 'no space' in the figures and cast as float
#The commas makes them seen as strings
#Tip: complete cast statement before fiilna
df["Debits"] = df["Debits"].str.replace(",", "").astype(float)
df["Credits"] = df["Credits"].str.replace(",", "").astype(float)
df["Balance"] = df["Balance"].str.replace(",", "").astype(float)
print(df.head())
print()

#Fill nan values with zero for accurate calculations
df.fillna(0, inplace=True)
print(df.head())
print()

#Write a format statement
#First, assign the variables
start = df["Trans. Date"][0]

end = df["Trans. Date"][(len(df)-1)]

credit = df["Credits"].sum()

debit = np.sum(df.Debits)

avg_bal = round(np.mean(df.Balance), 2)         #Round off to 2 decimal places

#The statement
print("This account statement starts from {} and ends {}".format(start,end))

print("\nTotal credit is {}".format(credit))    #'\n' means start on a new line

print("\nTotal debit is {}".format(debit))

print("\nAverage Acc Balance is {}".format(avg_bal))

#Print a better looking dataframe using tabulate
print()
print(tabulate(df.head(20), headers='keys', tablefmt='psql'))










