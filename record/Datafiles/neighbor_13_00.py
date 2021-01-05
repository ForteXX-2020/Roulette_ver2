# -*- coding: utf-8 -*-
"""
neighbor 13_00_roulette
"""

import numpy as np
import pandas as pd


count_matrix = np.zeros((38,38))
neighbor_matrix = pd.read_excel("./neighbor_13_00.xlsx")
neighbor_matrix = neighbor_matrix.set_index("main")


df = pd.read_csv("./exportData_UTF-8_1109_Hardrock.csv","r",names=["value"])
df = df.replace(100, 37)
df_length = len(df)-1


for i in range(1,df_length):
    x = df.iloc[i, 0]
    y = df.iloc[i-  1, 0]

    for j in range(1,14):
        count_matrix[y,neighbor_matrix.loc[x,j]] = count_matrix[y,neighbor_matrix.loc[x,j]] + 1

