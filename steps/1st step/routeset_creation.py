import csv
import numpy as np

with open('reduced_route_erorfree2.csv','r') as readobj:
    list1 = list(csv.reader(readobj))

set1 = []
for i in range(100):
    set1.append(list1[i])
filepoint = open('set1.csv','a')
for i in range(len(set1)):
    filepoint.writelines(["%s," % item1 for item1 in set1[i]])
    filepoint.writelines("\n")
#print(len(set1))

set2 = []
for i in range(100,200):
    set2.append(list1[i])
filepoint = open('set2.csv','a')
for i in range(len(set2)):
    filepoint.writelines(["%s," % item1 for item1 in set2[i]])
    filepoint.writelines("\n")
#print(set2)

set3 = []
for i in range(200,300):
    set3.append(list1[i])
filepoint = open('set3.csv','a')
for i in range(len(set3)):
    filepoint.writelines(["%s," % item1 for item1 in set3[i]])
    filepoint.writelines("\n")
#print(len(set3))

set4 = []
for i in range(300,400):
    set4.append(list1[i])
filepoint = open('set4.csv','a')
for i in range(len(set4)):
    filepoint.writelines(["%s," % item1 for item1 in set4[i]])
    filepoint.writelines("\n")
#print(set4)

set5 = []
for i in range(400,500):
    set5.append(list1[i])
filepoint = open('set5.csv','a')
for i in range(len(set5)):
    filepoint.writelines(["%s," % item1 for item1 in set5[i]])
    filepoint.writelines("\n")
#print(set5)
set6 = []
for i in range(500,592):
    set6.append(list1[i])

filepoint = open('set6.csv','a')
for i in range(len(set6)):
    filepoint.writelines(["%s," % item1 for item1 in set6[i]])
    filepoint.writelines("\n")
#print(set6)