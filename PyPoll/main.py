import os
import csv

#create some variables
voter = []
county = []
candidate = []
result_dic = {}

#bring in our csv file
csvpath = os.path.join('election_data.csv')

#read the csv file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #pull out the header and print it
    csv_header = next(csvreader)
    print(f'CSV header: {csv_header}')

    #loop through each row in the file
    for row in csvreader:
        #store each VoterID value into a list voter
        voter.append(row[0])
        #sotre each Candidate value into a list candidate
        candidate.append(row[2])

    #get the total number of voters by getting the length of the voter list and print that value
    numberOfVoters = len(voter)
    print(f'Total Votes: {numberOfVoters}')

    #a set will only take unique values from the list, then store that as a list
    unique_candidates = list(set(candidate))
    #print(unique_candidates)

    #loop through the uniue candidate list 
    for name in unique_candidates:
        #create some new variables
        votecount = 0
        votepercent = 0
        #loop through the entire list of candidates
        for can in candidate:
            #check for when the the candidate names are equal
            if can == name:
                #add up the times they are equal
                votecount += 1
                #get the percentage from the number of total votes
                votepercent = (votecount/len(candidate)) * 100
        #create a dictionary from the unique names, percent of votes they got, and the count of votes they got
        result_dic[name] = votepercent, votecount

    print(result_dic)

    #find the winner by checking for the max value
    max_value = max(result_dic.values())
    #then find the winner name by looking for the key with that max value
    max_key = [k for k, v in result_dic.items() if v == max_value]
    print(max_key)
