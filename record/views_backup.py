from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day
from django_pandas.io import read_frame
import numpy as np
import pandas as pd


def index(request):
    context = {
        'list':Day.objects.all()
    }
    return render(request, 'record/list.html',context)

def add(request):
    form = DayCreateForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
        form.save()
        return redirect('record:index')
 
    context = {
        'form':DayCreateForm()
    }
    return render(request,'record/form.html',context)



def update(request, pk):
    day = get_object_or_404(Day, pk=pk)
    form = DayCreateForm(request.POST or None, instance = day)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('record:index')
    
    context = {
        'form':form
    }
    return render(request,'record/form.html', context)

def delete(request, pk):
    day = get_object_or_404(Day, pk=pk)
    if request.method == 'POST':
        day.delete()
        return redirect('record:index')
    
    context = {
        'day':day
    }
    return render(request,'record/day_delete_confirm.html', context)


def all_delete(request):
    if request.method == 'POST':
        Day.objects.all().delete()

    context= {}

    return render(request,'record/all_delete_confirm.html', context)

def next_matrix(request):
    if request.method == 'POST':
        Days = Day.objects.all()
        df_all = read_frame(Days, fieldnames = ['date', 'number', 'types', 'place', 'company'])
        df = df_all.number

        count_matrix = np.zeros((38,38))
        neighbor_matrix = np.array([[	14	,	2	,	0	,	28	,	9	]	,
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
[		13	,	1	,	37	,	27	,	10	]	])

        results_matrix = np.array([[	2	,	0	],
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
[	14	,	0	]])


        
        df = df.replace(100, 37)
        df_length = len(df)-1
        
        for i in range(1, df_length):
            x = df.iloc[i]
            y = df.iloc[i-  1]
            
            for j in range(5):
                count_matrix[y,neighbor_matrix[x,j]] = count_matrix[y,neighbor_matrix[x,j]] + 1
                
                now = df.tail()
                next_numbers = count_matrix[now,:]
                
        for l in range(38):
            m = results_matrix[l,0]   
            n = next_numbers[m]    
            results_matrix[l,1] = n
    
       
        results = results_matrix         
        my_app = {'result' : results}
        return render(request,'record/next_matrix.html', my_app)

    context = {}
    return render(request,'record/next_matrix.html', context)

###DFバージョン
def next_matrix(request):
    if request.method == 'POST':
        Days = Day.objects.all()
        df_all = read_frame(Days, fieldnames = ['date', 'number', 'types', 'place', 'company'])
        df = df_all.number



        count_matrix = np.zeros((38,38))
        nm_data = [[	0	,	14	,	2	,	0	,	28	,	9	]	,
[	1	,	36	,	13	,	1	,	37	,	27	]	,
[	2	,	35	,	14	,	2	,	0	,	28	]	,
[	3	,	34	,	15	,	3	,	24	,	36	]	,
[	4	,	33	,	16	,	4	,	23	,	35	]	,
[	5	,	32	,	17	,	5	,	22	,	34	]	,
[	6	,	31	,	18	,	6	,	21	,	33	]	,
[	7	,	30	,	11	,	7	,	20	,	32	]	,
[	8	,	29	,	12	,	8	,	19	,	31	]	,
[	9	,	0	,	28	,	9	,	26	,	30	]	,
[	10	,	37	,	27	,	10	,	25	,	29	]	,
[	11	,	26	,	30	,	11	,	7	,	20	]	,
[	12	,	25	,	29	,	12	,	8	,	19	]	,
[	13	,	24	,	36	,	13	,	1	,	37	]	,
[	14	,	23	,	35	,	14	,	2	,	0	]	,
[	15	,	22	,	34	,	15	,	3	,	24	]	,
[	16	,	21	,	33	,	16	,	4	,	23	]	,
[	17	,	20	,	32	,	17	,	5	,	22	]	,
[	18	,	19	,	31	,	18	,	6	,	21	]	,
[	19	,	12	,	8	,	19	,	31	,	18	]	,
[	20	,	11	,	7	,	20	,	32	,	17	]	,
[	21	,	18	,	6	,	21	,	33	,	16	]	,
[	22	,	17	,	5	,	22	,	34	,	15	]	,
[	23	,	16	,	4	,	23	,	35	,	14	]	,
[	24	,	15	,	3	,	24	,	36	,	13	]	,
[	25	,	27	,	10	,	25	,	29	,	12	]	,
[	26	,	28	,	9	,	26	,	30	,	11	]	,
[	27	,	1	,	37	,	27	,	10	,	25	]	,
[	28	,	2	,	0	,	28	,	9	,	26	]	,
[	29	,	10	,	25	,	29	,	12	,	8	]	,
[	30	,	9	,	26	,	30	,	11	,	7	]	,
[	31	,	8	,	19	,	31	,	18	,	6	]	,
[	32	,	7	,	20	,	32	,	17	,	5	]	,
[	33	,	6	,	21	,	33	,	16	,	4	]	,
[	34	,	5	,	22	,	34	,	15	,	3	]	,
[	35	,	4	,	23	,	35	,	14	,	2	]	,
[	36	,	3	,	24	,	36	,	13	,	1	]	,
[	37	,	13	,	1	,	37	,	27	,	10	]	]
        nm_columns = [	'main'	,	'1'	,	'2'	,	'3'	,	'4'	,	'5'	]
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
        
        df = df.replace(100, 37)
        df_length = len(df)-1
        
        for i in range(1, df_length):
            x = df.iloc[i]
            y = df.iloc[i-  1]
            
            for j in range(5):
                count_matrix[y,neighbor_matrix.loc[x,j]] = count_matrix[y,neighbor_matrix.loc[x,j]] + 1
                
        now = df.tail()
        next_numbers = count_matrix[now,:]
                
        for l in range(38):
            m = results_matrix.loc[(results_matrix.number == l)]   
            n = m.index[0]    
            o = next_numbers[l]
            results = results_matrix.to_numpy()
            results[n,1] = o
    
       
        my_app = {'result' : results}
        return render(request,'record/next_matrix.html', my_app)

    context = {}
    return render(request,'record/next_matrix.html', context)
