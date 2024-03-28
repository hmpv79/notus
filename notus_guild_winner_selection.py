import random
import csv
from datetime import datetime

# Define the CSV filename
csv_filename = 'shards.csv'

# Read participant data from CSV file
participants = []
with open(csv_filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        participants.append(row)

# Calculate the priority for each participant
for participant in participants:
    # Convert date to datetime object
    date = datetime.strptime(participant["join_date"], "%Y-%m-%d")
    # Calculate the number of days since join date
    days_since_join = (datetime.now() - date).days
    # Calculate priority based on the number of shards and days since join date
    priority = int(participant["shards"]) * days_since_join
    participant["priority"] = priority

# Extract the priorities
priorities = [int(participant["priority"]) for participant in participants]

# Select a winner based on priorities
winner = random.choices(participants, weights=priorities, k=1)[0]

# Write the winner's name to an environment file
with open('winner.txt', 'w') as file:
    file.write(winner["participant"])
