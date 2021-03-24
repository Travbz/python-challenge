import os
import csv
csvpath = os.path.join('C:/Users/tbrid/Desktop/python-challenge/Pypoll/Resources/election_data.csv')
# create variables and assign initial values
total_vote = 0
candidates = {}
vote_percentage = 0
winner = 0
candidate = ''
votes_per = []
percent = []
winner = ''

with open(csvpath, 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    print(data)

     # Read the header row first (skip this step if there is now header)
    csv_header = next(data)
    
    #loop through rows in csvreader and read each row to find total rows
    for row in data:
        total_vote += 1
        if row[2] in candidates:
          candidates[row[2]] += 1
        else:
          candidates[row[2]] = 1
print(candidates)
print(total_vote)