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

