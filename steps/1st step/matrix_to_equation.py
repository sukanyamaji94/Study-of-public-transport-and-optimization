from csv import reader
# read csv file as a list of lists
with open('matrix_set_cover61.csv', 'r') as read_obj:
# pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
# Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
a = len(list_of_rows)
print(list_of_rows[0])

# read variable file in a list named x
with open('variables92.csv','r') as read_obj1:
    csv_reader = reader(read_obj1)
    list_of_var = list(csv_reader)
b= len(list_of_var)
#print(list_of_var)

filepoint = open('constraint_equations6.txt','a')

for i in range(92):
    for j in range(74):
        if(list_of_rows[i][j]=='1'):
            filepoint.write(list_of_var[0][j]+' + ')
    filepoint.write('\t<=1')
    filepoint.write('\n')
    filepoint.write('\n')








