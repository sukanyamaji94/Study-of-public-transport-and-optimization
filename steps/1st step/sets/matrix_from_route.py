from csv import reader
# read csv file as a list of lists
with open('set6.csv', 'r') as read_obj:
# pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
# Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
a = len(list_of_rows)
print(a)
node = ['routes', 0, 1]
for i in range(2, 74):
    node.append(i)
#print(node)
arr2 = []
arr = [0]
for i in range(1,74):
    arr.append(0)
#print(arr)
arr2 = arr
file_point = open('matrix_set_cover6.csv', 'a')
file_point.write(node[0])
file_point.write(",")
file_point.writelines(["%d, " % item1 for item1 in range(0,74)])
file_point.write("\n")
for i in range(0, a):
    l1 = list_of_rows[i]
    print(l1)
    arr.clear()
    for j in range(0, 74): # array initialization for the loop
        arr.append(0)
    for item in l1:
        if arr[int(item)] == arr2[int(item)] and arr2[int(item)]== 1:
            break
        else:
            arr[int(item)] = 1
    arr2 = arr

    file_point.write('"'+str(l1)+'",')#print(item)
    file_point.writelines(["%d, " % item1 for item1 in arr])
    file_point.write('\n')

#print(arr)