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
#Sami Coalson was majorly helpful, he deserves credit for helping me write my for loops and showing me the genius print() nested in a for loop.

with open(csvpath, 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    csv_header = next(data)
    #loop through rows in csvreader and read each row to find total rows
    for row in data:
        total_vote += 1
        # iterate through rows and find each distinct element in rows
        if row[2] in candidates:
          candidates[row[2]] += 1
        else:
          candidates[row[2]] = 1
#seperate compiled elements into a .keys list and .values list         
candidate = list(candidates.keys())         
votes_per = list(candidates.values())
for i in range(len(candidate)):
    vote_percentage.append((votes_per[i] / total_vote) * 100)
for i in range(len(votes_per)):
    if votes_per[i] > votes_per[winner_i]:
        winner_i = i


        
print("---Election Results---")
print("----------------------")
print(f"-Total Votes: {total_vote}-")
print("----------------------")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {round(vote_percentage[i], 3)}% ({votes_per[i]})")

print("----------------------")
print(f"Winner: {candidate[winner_i]}")
print("----------------------")

output_path = os.path.join('C:/Users/tbrid/Desktop/python-challenge/Pypoll/Resources/election_data.csv')
with open(output_path, 'w') as txtfile:
    print("---Election Results---")
    print("----------------------")
    print(f"-Total Votes: {total_vote}-")
    print("----------------------")
    for i in range(len(candidate)):
        print(f"{candidate[i]}: {round(vote_percentage[i], 3)}% ({votes_per[i]})")

    print("----------------------")
    print(f"Winner: {candidate[winner_i]}")
    print("----------------------")