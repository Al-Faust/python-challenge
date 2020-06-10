import os
import csv

#variables
total_votes = 0
candidate_name_check = ''
candidates = []
candidate_votes = {}

#winner
winner_name = ''
winner_votes = 0


#finding the orginial csv
csv_org = os.path.join("Resources", "election_data.csv")

#output txt
txt_output = os.path.join("Analysis", "analysis.txt")

with open(csv_org, 'r') as csv_org_file:
    csvreader = csv.reader(csv_org_file, delimiter =',')

    csvheader = next(csvreader)
    # print(csvheader)

    #store headers
    headers = next(csvreader)

    for row in csvreader:

        #get total votes
        total_votes += 1

        #get candidate name
        candidate_name_check = row[2]

        #check if current row candidate is in candidate list
        if candidate_name_check not in candidates:
            
            #append to list
            candidates.append(candidate_name_check)

            #track candidates votes
            candidate_votes[candidate_name_check] = 0

        #add votes to name
        candidate_votes[candidate_name_check] += 1

with open(txt_output, "w") as txt_analysis:

    election_results = (
        f'Election Results\n'
        f'\n'
        f'total votes: {total_votes}\n'
    )
    print(election_results)
    txt_analysis.write(election_results)

    #loop through candidate list
    for candidate in candidate_votes:

        #get vote count
        votes = candidate_votes.get(candidate)

        #get percentage
        percentage = float(votes) / float(total_votes) * 100
        

        #check if candidate beats current winning candidate
        if (votes > winner_votes):
            winner_votes = votes
            winner_name = candidate

            #get winner percentage
            winner_percentage = votes / total_votes * 100

        candidate_results = f'{candidate}: {percentage:.1f}% ({votes})\n'
        print(candidate_results)
        txt_analysis.write(candidate_results)

    winner_results = (
        f'\n'
        f'Winner: {winner_name}'
    )

    print(winner_results)
    txt_analysis.write(winner_results)