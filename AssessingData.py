# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:55:17 2023

@author: Amara
"""

import pandas as pd
import numpy as np
from tabulate import tabulate


df = pd.read_csv("post_natal_data.csv")

print(tabulate(df.head(), headers='keys', tablefmt='psql'))

print(df.tail())

print(df.sample())

print(df.info())

print(df.isnull().sum())


