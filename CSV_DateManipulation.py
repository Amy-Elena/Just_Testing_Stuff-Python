# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 19:13:11 2023

@author: Amara
"""

#Import packages
import pandas as pd
import numpy as np
from tabulate import tabulate
import calendar

#Read csv
df = pd.read_csv("outfile.csv")
print(df.head())
print()

#Drop irrelevant columns
df.drop(columns=["Remarks", "Value. Date", "Reference", "Originating Branch"], axis=1, inplace=True)
print(df)
print()

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

#See data type for 'Trans.Date'
print(df["Trans. Date"].dtype)

#Convert to datetime format
df["Trans. Date"]= pd.to_datetime(df["Trans. Date"])
print(df["Trans. Date"])
print()

#Now in datetime format, then use 'dt' (datetime) to manipualte date
#Separate date from datetime into a new column with attribute 'date'
df["Date"]= df["Trans. Date"].dt.date

print(tabulate(df.head(20), headers='keys', tablefmt='psql'))
print()

#Extract day of week of a date using function 'day_name'
df["Day_of_week"]= df["Trans. Date"].dt.day_name()

print(tabulate(df.head(10), headers='keys', tablefmt='psql'))
print()

#Extract month of a date into a new column
df["Month"]= df["Trans. Date"].dt.month

print(tabulate(df.head(10), headers='keys', tablefmt='psql'))
print()

#With '.dt.month', month appears as a number eg june shows as 6
#Use 'calendar' to get month name
d = dict(enumerate(calendar.month_abbr))
df["Month_name"] = df["Month"].map(d)

print(tabulate(df.head(10), headers='keys', tablefmt='psql'))
print()

#Export cleaned CSV
#Set index to false so new index is not created by pandas
#Also, so date nmanipulations wont be lost
df.to_csv("outfile_clean.csv",index=False)


















