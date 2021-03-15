# Objective 1: Import modules os and csv
import os
import csv
# Objective 2: Set the path for the CSV file 
PyBankcsv = os.path.join("budget_data.csv")
# Objective 3: Create the lists to store data. 
profit = []
monthly_changes = []
date = []
# Initialize the variables as required.
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
# Open the CSV
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Iterating
    for row in csvreader:    
      # Use count to count the number months in this dataset. Variable modified
      count = count + 1 # position shift, look at data csv
      # Needed to collect the changes in profits
      date.append(row[0]) # position shift, look at data csv
# Append the profit information & calculate the total profit
      profit.append(row[1])
      total_profit = total_profit + int(row[1]) # position shift, look at data csv
#Calculate the average change in profits from month to month, then calulate the average change in profits
      final_profit = int(row[1]) #int(row[1]) run cell 0
      monthly_change_profits = final_profit - initial_profit #calculates change from month to month
      #Store in monthly changes in a list
      monthly_changes.append(monthly_change_profits) #changes monthly changes list after calculations
      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit
      #Calculate the average change in profits
      average_change_profits = (total_change_profits/count) #count = count + 1
      #Find the max and min change in profits and the corresponding dates these changes were obeserved
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)
      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
    print("Financial Analysis")
    print("Total Months: " + str(count)) #rows in date column
    print("Total Profits: " + "$" + str(total_profit)) #rows in Profits/losses column
    print("Average Change: " + "$" + str(int(average_change_profits))) #variables entered in as integers entered in as strings
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")#variables entered in as integers entered in as strings
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")#variables entered in as integers entered in as strings


with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")