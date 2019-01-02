# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:54:39 2018

@author: Michael Er Jun Li 
"""

import pandas as pd #import panda library 
import matplotlib.pyplot as plt
import numpy as np

#Loading raw data set from Github URL
url = "https://raw.githubusercontent.com/mlej8/mais-202-coding-challenge/master/data.csv"
data = pd.read_csv(url, usecols=['int_rate','purpose']) #Using panda's read_csv function to read the excel document. Using the 'usecols =' to filter out the columns we want i.e. int_rate and purpose

#Grouping our dataframe by the 'purpose' column and then doing the average of their interest rates 
avg = data.groupby(['purpose'])['int_rate'].mean()

#Transforming avg which is a type series to a Dataframe
df = avg.to_frame().reset_index()

#Sort Dataframe df by interest rates from biggest to lowest
final_df = df.sort_values(by=['int_rate'], ascending = False)

#Rename final_df columns
final_df.columns = ['Purpose', 'avg_rate']

#Reset final_df index after sorting it and dropping old index
final_df = final_df.reset_index(drop = True)
print(final_df)

#Plotting final Dataframe into a bar graph and setting the x axis by the column purpose
graph = df.plot(kind='bar', title = 'Average Interest Rates by Purpose', legend = False, x = 'purpose')
x_axis = graph.set_xlabel('Purpose', fontsize = 12)
y_axis = graph.set_ylabel('Average Interest Rates', fontsize = 12)

