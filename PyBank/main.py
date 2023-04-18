# Importing modules
import os
import csv

# Reading the csv file and assigning path for txt file
BUDGET_CSV_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("Analysis", "output.txt")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Setting beginning values and creating dictionary that will dates as keys and changes in profit/losses as values
total_months = 0
total = 0
changes = {}
total_changes = 0

with open(BUDGET_CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Stores the header row
    next(csvreader) 
    for row in csvreader:
        date = row[0]
        profit_or_loss = int(row[1])
        # The total number of months included in the dataset
        total_months += 1
        total += profit_or_loss
        # The changes in "Profit/Losses" over the entire period
        try:
            change = profit_or_loss - prev_profit_or_loss
            # Populating changes dictionary
            changes[date] = change
            prev_profit_or_loss = profit_or_loss
        except NameError:
            prev_profit_or_loss = profit_or_loss

for date, change in changes.items():
    # The average of the "Profit/Losses" changes
    total_changes += change
    average_changes = round(total_changes / len(changes), 2)
    # The greatest increase in profits (date and amount) over the entire period
    try:
        if change > greatest_increase_amt:
            greatest_increase_amt = change
            greatest_increase_date = date
    except NameError:
        greatest_increase_amt = change
    # The greatest decrease in profits (date and amount) over the entire period
    try:
        if change < greatest_decrease_amt:
            greatest_decrease_amt = change
            greatest_decrease_date = date
    except NameError:
        greatest_decrease_amt = change

# Assign results to a variable
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_changes}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amt})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amt})\n"
)

# Print results to terminal exports results to txt file
print(output)
with open(OUTPUT_PATH, 'w') as outputfile:
    outputfile.write(output)