import csv
with open('studentdetails.csv','r')as csv_file1:
    csv_reader=csv.DictReader(csv_file1)
    for line in csv_reader:
        print(line)
