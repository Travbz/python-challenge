import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')




with open(csvpath, 'r') as csvfile:
 # CSV reader specifies delimiter and variable that holds contents
  csvreader = csv.reader(csvfile, delimiter=',')
  print(csvreader)

     #for row in csvreader:

