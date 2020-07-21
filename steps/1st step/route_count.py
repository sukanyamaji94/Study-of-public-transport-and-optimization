import csv
import numpy as np

with open('available_routes.csv','r') as readobj:
    list1 = list(csv.reader(readobj))
#print(list1)

with open('nodewise_demand1.txt','r') as readobj1:
    demand = list(csv.reader(readobj1))
a=[]
for i in range(len(demand)):
    a.append(int(demand[i][0]))
print(a)
b =[]
for i in range(592):
    b.append(i)
filepoint = open('demand_routewise1.csv','a')

'''for j in range(len(list1[0])):
    arr.append(int(list1[0][j]))
print(arr)'''
for i in range(len(list1)):
    for j in range(len(list1[i])):
        c = list1[i][j]
        print(c)
        b[i]= b[i] + a[int(c)]
    filepoint.writelines(str(i)+',' +str(b[i]))
    filepoint.writelines('\n')





