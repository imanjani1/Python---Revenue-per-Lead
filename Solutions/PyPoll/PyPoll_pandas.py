# Imports
import os
import pandas as pd

# Define the file path
csvpath = os.path.join('raw_data', 'election_data_2.csv')

# Create the data frame
df = pd.read_csv(csvpath)

# Calculate total number of votes
total_votes = df['Voter ID'].count()

# Count votes
counts = df['Candidate'].value_counts()
print(counts)

# Find winner
winner = counts.idxmax()

# Print output
output = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

for candidate, count in counts.iteritems():
    output += f'{candidate}: {count/total_votes*100:.3f}% ({count})\n'

output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

print(output)
