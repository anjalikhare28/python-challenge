import csv

total_votes = 0
candidates = []
votes = []
vote_percentages = []
candidate = ""
index = 0
winner_candidate = ""
winner_votes = 0
winner_index = 0


with open("C:\\Users\\Sweety\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\\election_data.csv") as infile,\
        open ("C:\\Users\\Sweety\\Documents\\GitHub\\python-challenge\\PyPoll\\Analysis\\result.txt","w") as outfile:
   reader = csv.reader(infile)

   next(reader, None)  # skip the headers
   for row in reader:
       candidate = row[2]
       total_votes += 1
       #print(total_votes)
       if candidate in candidates:
           index = candidates.index(candidate)
           votes[index] = votes[index] + 1
           #print(index)    
       else:
           candidates.append(candidate)
           votes.append(1)

       #print(candidate)
       #print(candidates)
       #print(votes) 

       #if total_votes > 10:
       #    break

   #print(range(len(candidates)))
   for index in range(len(candidates)):
       vote_percentage = votes[index]/total_votes*100
       vote_percentages.append(vote_percentage)

       if votes[index] > winner_votes:
           winner_votes = votes[index]
           winner_index = index
           #winner_candidate = candidates[winner_index]    
   
   result = '''   Election Results
   -----------------------------------
   Total Votes: {}    
   -----------------------------------
   '''.format(total_votes)
   
   for index in range(len(candidates)):
       result += '''{}: {:.3f}% ({}) 
   '''.format(candidates[index],vote_percentages[index],votes[index])
   
   result += '''-----------------------------------
   Winner: {}
   -----------------------------------'''.format(candidates[winner_index])

   outfile.write(result) 
   print(result)   
        