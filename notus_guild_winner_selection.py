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

# Print participants and their weights
print("Participant and their weights:")
for participant in participants:
    print(f"{participant['participant']}: {participant['priority']}")

# Extract the priorities
priorities = [int(participant["priority"]) for participant in participants]

# Select a winner based on priorities
winner = random.choices(participants, weights=priorities, k=1)[0]

print("\nDraw Winner:", winner["participant"])

# Print the winner's name for GitHub Actions output
print(f"::set-output name=winner::{winner['name']}")
