import csv

csv_in = open ('table_in.csv', 'r')
reader = csv.reader(csv_in, skipinitialspace=True, delimiter=',')

with open('table_out.csv', 'w') as csv_out:
    out = csv.writer(csv_out, skipinitialspace=True, delimiter=',')
    for row in reader:
        line = [row[1], row[0]]
        out.writerow(line)
        print(line)
