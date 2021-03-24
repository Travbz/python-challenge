import os
import csv
csvpath = os.path.join('C:/Users/tbrid/Desktop/python-challenge/Pypoll/Resources/election_data.csv')

total_vote = 0
candidates = []
vote_percentage = 0
winner = 0
candidate = {}


with open(csvpath, 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    print(data)

     # Read the header row first (skip this step if there is now header)
    csv_header = next(data)
    
    #loop through rows in csvreader and read each row
    for row in data:
        total_vote += 1

    for elem in data:
        if elem[2] not in candidates:
            candidates[elem[2]] = 0
        else:
            candidates[elem[2]] = candidates[elem[2]] + 1
           
print(candidates)



# iterate over the list and use each distinct element of the list as a key of the dictionary and store the corresponding count of that key as values
'''def CountFrequency(candidates):
    frequency = {}
    for candidate in candidates: #i created an empty fucking list
        if (candidate in frequency):
            frequency[candidate] += 1
        else:
            frequency[candidate] = 1

    for key, value in frequency.items():
        print("% d : % d"%(key, value))
    CountFrequency(candidates)'''
#tally total votes cast at election, discover for name each candidate

#compile numer of votes for each candidate

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

#https://www.geeksforgeeks.org/counting-the-frequencies-in-a-list-using-dictionary-in-python/