import numpy as np
import pandas as pd

count_matrix = np.zeros((38,38))
nm_data = [[	14	,	2	,	0	,	28	,	9	]	,
[		36	,	13	,	1	,	37	,	27	]	,
[		35	,	14	,	2	,	0	,	28	]	,
[		34	,	15	,	3	,	24	,	36	]	,
[		33	,	16	,	4	,	23	,	35	]	,
[		32	,	17	,	5	,	22	,	34	]	,
[		31	,	18	,	6	,	21	,	33	]	,
[		30	,	11	,	7	,	20	,	32	]	,
[		29	,	12	,	8	,	19	,	31	]	,
[		0	,	28	,	9	,	26	,	30	]	,
[		37	,	27	,	10	,	25	,	29	]	,
[		26	,	30	,	11	,	7	,	20	]	,
[		25	,	29	,	12	,	8	,	19	]	,
[		24	,	36	,	13	,	1	,	37	]	,
[		23	,	35	,	14	,	2	,	0	]	,
[		22	,	34	,	15	,	3	,	24	]	,
[		21	,	33	,	16	,	4	,	23	]	,
[		20	,	32	,	17	,	5	,	22	]	,
[		19	,	31	,	18	,	6	,	21	]	,
[		12	,	8	,	19	,	31	,	18	]	,
[		11	,	7	,	20	,	32	,	17	]	,
[		18	,	6	,	21	,	33	,	16	]	,
[		17	,	5	,	22	,	34	,	15	]	,
[		16	,	4	,	23	,	35	,	14	]	,
[		15	,	3	,	24	,	36	,	13	]	,
[		27	,	10	,	25	,	29	,	12	]	,
[		28	,	9	,	26	,	30	,	11	]	,
[		1	,	37	,	27	,	10	,	25	]	,
[		2	,	0	,	28	,	9	,	26	]	,
[		10	,	25	,	29	,	12	,	8	]	,
[		9	,	26	,	30	,	11	,	7	]	,
[		8	,	19	,	31	,	18	,	6	]	,
[		7	,	20	,	32	,	17	,	5	]	,
[		6	,	21	,	33	,	16	,	4	]	,
[		5	,	22	,	34	,	15	,	3	]	,
[		4	,	23	,	35	,	14	,	2	]	,
[		3	,	24	,	36	,	13	,	1	]	,
[		13	,	1	,	37	,	27	,	10	]	]
nm_columns = [	'1'	,	'2'	,	'3'	,	'4'	,	'5'	]


neighbor_matrix = pd.DataFrame(data = nm_data, columns = nm_columns)

rm_data = [[	2	,	0	],
[	0	,	0	],
[	28	,	0	],
[	9	,	0	],
[	26	,	0	],
[	30	,	0	],
[	11	,	0	],
[	7	,	0	],
[	20	,	0	],
[	32	,	0	],
[	17	,	0	],
[	5	,	0	],
[	22	,	0	],
[	34	,	0	],
[	15	,	0	],
[	3	,	0	],
[	24	,	0	],
[	36	,	0	],
[	13	,	0	],
[	1	,	0	],
[	37	,	0	],
[	27	,	0	],
[	10	,	0	],
[	25	,	0	],
[	29	,	0	],
[	12	,	0	],
[	8	,	0	],
[	19	,	0	],
[	31	,	0	],
[	18	,	0	],
[	6	,	0	],
[	21	,	0	],
[	33	,	0	],
[	16	,	0	],
[	4	,	0	],
[	23	,	0	],
[	35	,	0	],
[	14	,	0	]]

rm_columns = [	'number'	,	'value'	]
results_matrix = pd.DataFrame(data = rm_data, columns = rm_columns)


df = pd.read_csv("./exportData_UTF-8_1108_Hardrock.csv","r",names=["value"])
df = df.replace(100, 37)
df_length = len(df)-1

del nm_columns, nm_data, rm_columns, rm_data



for i in range(1,df_length):
    x = df.iloc[i, 0]
    y = df.iloc[i-  1, 0]

    for j in range(4):
        count_matrix[y,neighbor_matrix.loc[x,j]] = count_matrix[y,neighbor_matrix.loc[x,j]] + 1

def next_numbers(now):
    next_numbers = count_matrix[now,:]
    for l in range(38):
        m = results_matrix.loc[(results_matrix.number == l)]   
        n = m.index[0]    
        o = next_numbers[l]
        results = results_matrix.to_numpy()
        results[n,1] = o
    return results

print(next_numbers(5))


