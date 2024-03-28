import random
import csv
from datetime import datetime

# Define the CSV filename
csv_filename = 'participants.csv'

# Read participant data from CSV file
participants = []
with open(csv_filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        participants.append(row)

# Calculate the priority for each participant
for participant in participants:
    # Convert join date to datetime object
    join_date = datetime.strptime(participant["join_date"], "%Y-%m-%d")
    # Calculate the number of days since join date
    days_since_join = (datetime.now() - join_date).days
    # Calculate priority based on the number of shards and days since join date
    priority = int(participant["shards"]) * days_since_join
    participant["priority"] = priority

# Extract the priorities
priorities = [int(participant["priority"]) for participant in participants]

# Select a winner based on priorities
winner = random.choices(participants, weights=priorities, k=1)[0]

print("Winner:", winner["name"])
