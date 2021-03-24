import os
import csv
csvpath = os.path.join('C:/Users/tbrid/Desktop/python-challenge/Pypoll/Resources/election_data.csv')
# create variables and assign initial values
total_vote = 0
candidates = {}
vote_percentage = []
winner = 0
candidate = ''
votes_per = []
winner = ''
winner_i = 0
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
         
candidate = list(candidates.keys())         
votes_per = list(candidates.values())
for i in range(len(candidate)):
    vote_percentage.append((votes_per[i] / total_vote) * 100)


for i in range(len(votes_per)):
    if votes_per[i] > votes_per[winner_i]
    winner_i = i
    

        
print(winner)
# calc the percentage of votes per cand
# declare a winner
print(vote_percentage)
print(candidate)
print(votes_per)
 
#calc percentage for each candidate

#declare winner based on max vote

'''    * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------'''
print("---Election Results---")
print("----------------------")
print(f"-Total Votes: {total_vote}-")
print(candidates)

#https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/