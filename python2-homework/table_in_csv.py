import csv

with open('newcs.csv', 'w') as newfile:
    with open('table.csv', 'a') as oldfile:
        table_reader =csv.reader(newfile, delimiter=',')
        for i in table_reader:
            newfile.write(i[1])
            newfile.write(" ")
            newfile.write(1[0])
            newfile.write("\n")
