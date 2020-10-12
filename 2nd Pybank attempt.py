import os
import csv
# file path
csvfile = ("C:/Users/12172/nu-chi-data-pt-09-2020-u-c/03-Python/HW/Instructions/PyBank/Resources/budget_data.csv")

# set variables
MonthCount = 0
Total = 0
PL = []
monthList = []
monthlyChanges = []

# read input
with open(csvfile, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip first row which contains headers
    csvheader = next(csvreader)
    
    for row in csvreader:
        MonthCount += 1
        Total += int(row[1])
        PL.append(row[1])
        monthList.append(row[0])
# first month P&L value
firstPL = int(PL[0])

# this loop creates a list of monthly changes
for i in range(1, len(PL)):
    monthlyChanges.append(int(PL[i]) - firstPL)
    firstPL = int(PL[i])
    i += 1

AvgChange = sum(monthlyChanges) / len(monthlyChanges)


# find max and min increase
MaxIncrease = max(monthlyChanges)
MaxDecrease = min(monthlyChanges)

# find month index for the Max Increase and Max Decrease
for i in range(len(monthlyChanges)):
    if monthlyChanges[i] == MaxIncrease:
        maxIndex = (i - 1)
    elif monthlyChanges[i] == MaxDecrease:
        minIndex = (i - 1)
    else:
        i += 1
        
MaxMonth = monthList[maxIndex]
MinMonth = monthList[minIndex]



print("Financial Analysis")
print("-"*50)
print(f"Total Months: {MonthCount}")
print(f"Total: ${Total}")
print(f"Average Change: ${AvgChange}")
print(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")

# export
outputfile = 'summary.txt'

# use "\n" to create a new line
with  open(outputfile, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-"*50 + "\n")
    output.write(f"Total Months: {MonthCount}\n")
    output.write(f"Total: ${Total}\n")
    output.write(f"Average Change: ${AvgChange}")
    output.write(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})\n")
    output.write(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
