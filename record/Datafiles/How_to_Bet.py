# -*- coding: utf-8 -*-
"""
Train and Test
neighbor 13_00_roulette
"""

import numpy as np
import pandas as pd



neighbor_matrix = pd.read_excel("./neighbor_13_00.xlsx")
sequence_matrix = pd.read_excel("./Roulette_sequence_00.xlsx")
neighbor_matrix = neighbor_matrix.set_index("main")


df = pd.read_csv("./exportData_UTF-8_1108_Hardrock.csv","r",names=["value"])
df = df.replace(100, 37)
df_length = len(df)-1

count_matrix = np.zeros((38,38))    
for i in range(1,df_length):
    x = df.iloc[i, 0]
    y = df.iloc[i-  1, 0]

    for j in range(1,14):
        count_matrix[y,neighbor_matrix.loc[x,j]] = count_matrix[y,neighbor_matrix.loc[x,j]] + 1

now = 33
        
for l in range(0): 
    num = count_matrix[now,l]
    place = np.where(sequence_matrix == l)
    place = place[0]
    sequence_matrix.iloc[place,1] = num    

k = 188
pred = np.where(count_matrix[df.iloc[k, 0],:] == count_matrix[df.iloc[k, 0],:].max() )
win = df.iloc[k+1,0]
W = np.where(pred == win)
