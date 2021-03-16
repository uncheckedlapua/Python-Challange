# Objective 1: Import modules os and csv.
import os
import csv
# Objective 2: Set the path for the CSV file in PyPollcsv
PyPollcsv = os.path.join("election_data.csv")
# Objective 3: Create the lists to store data in. 
count = 0
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []
# Open the CSV using the set path PyPollcsv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
     #Iterations
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidate_list.append(row[2])
         # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidate_list):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidate_list.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
   
print("Election Results")   
print("Total Votes :" + str(count))    
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
            print("The winner is: " + winner)
# Print to a text file: election_results.txt
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("Total Vote: " + str(count) + "\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("The winner is: " + winner + "\n")
