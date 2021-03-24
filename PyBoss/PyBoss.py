import os
import csv
csvpath = os.path.join('C:/Users/tbrid/Desktop/du-virt-data-pt-03-2021-u-c/03-Python/HW/ExtraContent/Instructions/PyBoss/employee_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
     print(row)