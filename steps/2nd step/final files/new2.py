from csv import reader
# read csv file as a list of lists
with open('optimal routes.csv', 'r') as read_obj:
# pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
# Pass reader object to list() to get a list of lists
    list1 = list(csv_reader)

set1 = {}
for i in range(len(list1)):
    set1[i]=set(list1[i])

set2=set1
print(set2)
filepoint = open('transfer_detailsfinal1.csv','a')
for i in range(10):
    for j in range(10):
        value = set1[i].intersection(set2[j])
        if value==set():
            print("Null set")
            #filepoint.writelines("No link in between route ")
            #filepoint.writelines("%s, "%item for item in set1[i])
            #filepoint.writelines(" and route ")
            #filepoint.writelines("%s, "%item for item in set2[i])
            #filepoint.write("\n")
        if value==set1[i]:
            print(value)
            filepoint.writelines(" all node in ")
            filepoint.writelines("%s, "%item for item in set1[i])
            filepoint.writelines(" have zero transfer in between ")
            filepoint.writelines("\n")
        if (len(value)<=len(set1[i])) and value!=set() and value!=set1[i]:
            print(value)
            filepoint.writelines(" all node in nodes ")
            filepoint.writelines("%s, "%item for item in (set1[i]-value))
            filepoint.writelines(" and nodes ")
            filepoint.writelines("%s, "%item for item in (set2[j]-value))
            filepoint.writelines(" have one transfer in between \n")



