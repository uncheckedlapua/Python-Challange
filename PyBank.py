#Objectives!!!!!
# Create a Python script that analyzes the PyBank records to calculate each of the following:
# -->>  The total number of months included in the dataset
# -->>  The net total amount of "Profit/Losses" over the entire period
# -->>  The average of the changes in "Profit/Losses" over the entire period
# -->>  The greatest increase in profits (date and amount) over the entire period
# -->>  The greatest decrease in losses (date and amount) over the entire period
# -->>  Print the analysis to the terminal and export a text file with the results
#imports

import csv
import os
with open('budget_data.csv') as csv_file:
   csv_reader=csv.reader(csv_file)

   for line in csv_reader:
        print(line)
