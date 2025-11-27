import csv

csv_col=['Roll No','Name','House Name']

dict_data=[
    {'Roll No':1,'Name':'Alex','House Name':'India'},
    {'Roll No':2,'Name':'Aleena','House Name':'India'},
    {'Roll No':3,'Name':'Minu','House Name':'USA'},
    {'Roll No':4,'Name':'Ebin','House Name':'USA'},
    {'Roll No':5,'Name':'Jimmy','House Name':'India'}
]

csv_file="student.csv"

try:
    with open(csv_file,'w', newline='') as file1:
        writer = csv.DictWriter(file1, fieldnames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)
except IOError:
    print("I/O error")

data1 = csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
