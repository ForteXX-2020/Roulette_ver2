
# -*- coding: utf-8 -*-
"""
neighbor 11_00_roulette
"""

import numpy as np
import pandas as pd



count_matrix = np.zeros((38,38))
neighbor_matrix = pd.read_excel("./neighbor_11_00.xlsx")
results_matrix = pd.read_excel("./00Roulette.xlsx")
sequence_matrix = pd.read_excel("./Roulette_sequence_00.xlsx")
neighbor_matrix = neighbor_matrix.set_index("main")


df = pd.read_csv("./exportData_UTF-8_1108_Hardrock.csv","r",names=["value"])
df = df.replace(100, 37)
df_length = len(df)


for i in range(1,df_length):
    x = df.iloc[i, 0]
    y = df.iloc[i-  1, 0]

    for j in range(1,12):
        count_matrix[y,neighbor_matrix.loc[x,j]] = count_matrix[y,neighbor_matrix.loc[x,j]] + 1
'''
now = 15
        
for l in range(37): 
    num = count_matrix[now,l]
    place = np.where(sequence_matrix == l)
    place = place[0]
    sequence_matrix.iloc[place,1] = num 
    
''' 

def next_numbers(now):
    next_numbers = count_matrix[now,:]
    for l in range(38):
        m = results_matrix.loc[(results_matrix.number == l)]   
        n = m.index[0]    
        o = next_numbers[l]
        results = results_matrix.to_numpy()
        results[n,1] = o
    return results

print(next_numbers(36))