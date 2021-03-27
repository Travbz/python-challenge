import os

# Module for reading CSV files
import csv

#declaring the file path to file we want to read
csvpath = os.path.join('C:Users/tbrid/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

#assign starting value to variables
Total_Months = 0
Average_Change = 0
Increase = 0
Decrease = 0
Total = 0
DateI = " "
DateD = " "
numlist = []
difflist = []
totaldiff = 0
num_rows = 0
datelist = []
#open and read file
with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    # Create a PnL list(num_list) and a Datelist(datelist), count rows 
    for rows in csvreader: 
       num_rows += 1
       Total += int(rows[1])
       numlist.append(int(rows[1]))
       datelist.append(rows[0])

      # find month end value and subtract from previous month end
    for i in range(1, num_rows):
      difflist.append(numlist[i]-numlist[i - 1])

      #summing monthly differences to find total diff
    for i in range(len(difflist)):
      totaldiff += difflist[i]
      #loop through difflist to find greatest decrease and matching date
    for i in range(len(difflist)):
        if difflist[i] < Decrease:
            Decrease = difflist[i]
            DateD = datelist[i+1]
      #loop through difflist to find greatest Increase and matching date
        elif difflist[i] > Increase:
             Increase = difflist[i]
             DateI = datelist[i+1]

    Average_Change = round(totaldiff / len(difflist), 2)

print("Financial Analysis")
print("-------------------")
print(f"Total Months: {num_rows}")
print(f"Total: ${Total}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {DateI} (${Increase})")
print(f"Greatest Decrease in Profits: {DateD} (${Decrease})")

output_path = os.path.join('budget_analysis.txt')
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------\n")
    txtfile.write(f"Total Months: {num_rows}\n")
    txtfile.write(f"Total: ${Total}\n")
    txtfile.write(f"Average Change: ${Average_Change}\n")
    txtfile.write(f"Greatest Increase in Profits: {DateI} (${Increase})\n")