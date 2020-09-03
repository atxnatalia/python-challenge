import csv
import os

path = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

output = os.path.join("..", "PyPoll", "Analysis.txt")

total_votes = 0
candidate_choices = []
candidate_votes = {}
candidate_winner = ""
pop_vote_winner = 0

with open(path) as election_data:
    reader = csv.reader(election_data)
    
    header = next(reader)

    for row in reader:

        print(". ", end=""),


        total_votes = total_votes + 1
        candidate_name = row[2]

        
        if candidate_name not in candidate_choices:

            candidate_choices.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
            
        
with open(output, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"---------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------------\n")
    print(election_results, end="")

    
    txt_file.write(election_results)

   
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        
        if (votes > pop_vote_winner):
            pop_vote_winner = votes
            candidate_winner = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        txt_file.write(voter_output)

    candidate_winner_summary = (
        f"---------------------------------\n"
        f"Winner: {candidate_winner}\n"
        f"---------------------------------\n")
    print(candidate_winner_summary)

    txt_file.write(candidate_winner_summary)
