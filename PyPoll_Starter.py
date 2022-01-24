
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis2.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
county_options = []
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_county = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        county_name = row[1]
        # If county does not match any existing county add it the
        # the county list.
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
        # Add a vote to that county's count
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
   

for county_name in county_votes:
    # Retrieve vote count and percentage. 
    votes = county_votes[county_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print each county, their voter count, and percentage to the
    # terminal.
    county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

    print(county_results)
    txt_file.write(county_results)
    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_county = county_name
        winning_percentage = vote_percentage
# Print the winning county' results to the terminal.
winning_county = (
     f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")

print(winning_county)
txt_file.write(winning_county)