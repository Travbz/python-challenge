import os
import csv
from datetime import datetime
name = []
first_name = []
last_name = []
employeeID = []
ssn = []
new_ssn = []
state = []
dob = []
states = []
#https://gist.github.com/rogerallen/1583593 for state abbrev
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'}

csvpath = os.path.join('C:/Users/tbrid/Desktop/python-challenge/PyBoss/employee_data.csv')

with open(csvpath, "r") as csvfile:

   
   
    csvreader = csv.reader(csvfile, delimiter=',')
    csvfile.readline()
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
      employeeID.append(row[0])
      name= row[1].split(" ")
      first_name.append(name[0])
      last_name.append(name[1])
      date_split = row[2].split("-")
      dob.append(f"{date_split[1]}/{date_split[2]}/{date_split[0]}")
      ssn = row[3].split("-")
      new_ssn.append(f"***-**{ssn[2]}")
      state = row[4]
      states.append(f'{us_state_abbrev[state]}')


outpath = os.path.join('C:/Users/tbrid/Desktop/python-challenge/PyBoss/pybossanalysis.csv')
with open(outpath, "w", newline='') as csvfile:
   csvwriter = csv.writer(csvfile, delimiter =',')
   csvwriter.writerow(['Emp Id', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

   index=0
   while index < len(employeeID):
     csvwriter.writerow([employeeID[index], first_name[index], last_name[index], dob[index], new_ssn[index], states[index]])
     index += 1

print(employeeID)
print(first_name)
print(last_name)
print(dob)
print(new_ssn)
print(states)




