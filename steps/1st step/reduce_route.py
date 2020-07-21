from csv import reader

with open('route.txt','r') as readobj:
    list1 = list(reader(readobj))

#print(len(list1[1]))
filepoint = open('reduced_route19.csv','a')
for i in range(len(list1)):
    a= len(list1[i])
    b= len(list1[i])
    if(a<15 and b>10):
        filepoint.writelines("Route no: ")
        filepoint.writelines(str(i))
        filepoint.writelines("\n")
        filepoint.writelines(["%s, " % item1 for item1 in list1[i]])
        filepoint.writelines("\n")
