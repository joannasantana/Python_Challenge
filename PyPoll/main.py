# Importing modules 
import os
import csv
import collections

# Reading the csv file and assigning path for txt file
ELECTION_DATA_CSV_PATH = os.path.join("Resources", "election_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "output.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Set up a counter that will create a dictionary with candidate name as keys and # of votes as values
candidate_results = collections.Counter()

with open(ELECTION_DATA_CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Stores the header row
    next(csvreader) 
    for row in csvreader:
        # Count each vote + update the dictionary
        candidate_results[row[2]] += 1

# The total number of votes cast
total_votes = candidate_results.total()

# The percentage and total number of votes each candidate won
votes_per_candidate = ""
for candidate, votes in candidate_results.items():
    percent_votes = round((votes/total_votes) * 100, 3)
    votes_per_candidate += f"{candidate}: {percent_votes}% ({votes})\n"
    # The winner of the election based on popular vote
    try:
        if votes > most_votes:
            most_votes = votes
            winner = candidate
    except NameError:
        most_votes = votes

# Assign results to a variable
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    f"{votes_per_candidate}\n"
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print results to terminal exports results to txt file
print(output)
with open(OUTPUT_PATH, 'w') as outputfile:
    outputfile.write(output)


