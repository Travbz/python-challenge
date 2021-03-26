import os
import csv
from datetime import datetime
name = []
first_name = ''
last_name = ''
new_date = []
employeeID = 0
ssn = ''
new_ssn = []
state = []
new_state = []
year = 0
month = 0
day = 0

csvpath = os.path.join('C:/Users/tbrid/Desktop/python-challenge/PyBoss/employee_data.csv')
outpath = os.path.join('C:/Users/tbrid/Desktop/python-challenge/PyBoss/pybossanalysis.csv')
with open(csvpath, "r") as csvfile:
  with open(outpath, "w") as csvout:
    pyboss = csv.writer(csvfile, delimiter =',')
    csvwriter = csv.writer(csvout, lineterminator='\n')
    csvreader = csv.reader(csvfile, delimiter=',')
    csvfile.readline()
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
      name= row[1].split(" ")
      first_name = name[0]
      last_name = name[1]
      date_split = row[2].split("-")
      year = date_split[0]
      month = date_split[1]
      day = date_split[2]
      print(month,'/' day,'/'year)
      new_date =[month,day,year]
      #print(new_date)
